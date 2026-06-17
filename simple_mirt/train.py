"""
Train the compensatory multidimensional IRT model using SVI or MCMC.

This file handles the complete training process:
1. Read player responses from a CSV file.
2. Fit the statistical model defined in simple_mirt/model.py.
3. Print a short summary of the fitted model.
4. Save the fitted player and question values to CSV files.
"""

# argparse reads options supplied in the terminal, such as "--device cuda".
import argparse
# Path makes it easier to build file and directory paths.
from pathlib import Path

# pandas reads and writes table-shaped data, including CSV files.
import pandas as pd
# Pyro provides tools for defining and fitting probabilistic models.
import pyro
# PyTorch provides tensors and GPU support.
import torch
from pyro.infer import MCMC, NUTS, SVI, Trace_ELBO
from pyro.infer.autoguide import AutoNormal
from pyro.optim import ClippedAdam

# Import the MIRT model from the same directory.
from model import model


# Keep shared data and outputs at the project root.
PROJECT_ROOT = Path(__file__).parent.parent
DEFAULT_DATA_PATH = PROJECT_ROOT / "data" / "response_matrix.csv"
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "results"


def load_data(csv_path: str | Path, device="cpu"):
    """Load the response matrix and convert it into PyTorch tensors."""
    # The first CSV column contains player IDs, so use it as the row index.
    df = pd.read_csv(csv_path, index_col=0)

    # mask is True where an answer exists and False where the CSV cell is empty.
    # The model uses it to ignore questions that a player never encountered.
    mask = torch.tensor(df.notna().values, dtype=torch.bool, device=device)

    # PyTorch tensors cannot contain empty CSV cells for this model. Replace
    # empty cells with 0, knowing that mask will prevent the model from using them.
    responses = torch.tensor(df.fillna(0.0).values, dtype=torch.float32, device=device)

    # Also return the IDs so trained values can later be matched to players and questions.
    return responses, mask, df.index.astype(str).tolist(), df.columns.astype(str).tolist()


def train_svi(responses, mask, n_dimensions=2, n_steps=1000, lr=0.05):
    """
    Fit the model with SVI, a fast approximation method.

    SVI is generally faster than MCMC, but its uncertainty estimates may be less
    accurate because it approximates the full posterior probability distribution.
    """
    # Remove any parameters left over from a previous Pyro training run.
    pyro.clear_param_store()

    # The guide is Pyro's approximation of the unknown model parameters.
    guide = AutoNormal(model)
    # The optimizer controls how quickly SVI changes its estimated parameters.
    optimizer = ClippedAdam({"lr": lr})
    # Trace_ELBO measures how well the guide approximates the model posterior.
    svi = SVI(model, guide, optimizer, loss=Trace_ELBO())

    # Each step updates the estimated parameters once.
    for step in range(n_steps):
        loss = svi.step(responses, mask, n_dimensions)
        if step % 100 == 0:
            print(f"step {step:4d}  ELBO loss: {loss:,.1f}")

    # Return the fitted guide so its parameter estimates can be read later.
    return guide


def train_mcmc(
    responses, mask, n_dimensions=2, num_samples=500, warmup_steps=200, num_chains=1
):
    """
    Fit the model with MCMC using the No-U-Turn Sampler (NUTS).

    Warmup steps help NUTS tune itself and are discarded. After warmup, each
    chain creates num_samples possible sets of model parameters. Multiple chains
    are useful for checking whether MCMC reached similar results independently.
    """
    pyro.clear_param_store()

    # NUTS decides how to explore possible parameter values efficiently.
    kernel = NUTS(model)

    # Multiple GPU chains run in separate processes. "spawn" lets every process
    # initialize CUDA safely; Linux's default "fork" causes CUDA errors here.
    mp_context = "spawn" if responses.is_cuda and num_chains > 1 else None

    # Configure the MCMC run.
    mcmc = MCMC(
        kernel,
        num_samples=num_samples,
        warmup_steps=warmup_steps,
        num_chains=num_chains,
        mp_context=mp_context,
    )

    # Start training. This is where nearly all MCMC run time is spent.
    mcmc.run(responses, mask, n_dimensions)
    return mcmc


def posterior_median(fitted_model):
    """
    Choose one final value for every estimated parameter.

    A posterior contains many possible values. The median is the middle value
    and gives us a simple result to print and save.
    """
    if isinstance(fitted_model, MCMC):
        # MCMC returns many samples per parameter, so find each parameter's median.
        return {
            name: samples.median(dim=0).values
            for name, samples in fitted_model.get_samples().items()
        }

    # An SVI guide knows how to calculate its own median estimates.
    return fitted_model.median()


def save_results(output_dir, player_ids, question_ids, theta, alpha, d):
    """Write posterior median model parameters to CSV files."""
    # Create the results directory if it does not exist yet.
    output_dir.mkdir(parents=True, exist_ok=True)
    players_path = output_dir / "players.csv"
    questions_path = output_dir / "questions.csv"

    # detach() removes PyTorch's gradient tracking. cpu() moves GPU values back
    # to normal memory. numpy() converts them into values pandas can write.
    player_results = {"player_id": player_ids}
    for dimension in range(theta.shape[1]):
        player_results[f"theta_{dimension + 1}"] = (
            theta[:, dimension].detach().cpu().numpy()
        )
    pd.DataFrame(player_results).to_csv(players_path, index=False)

    question_results = {"question_id": question_ids}
    for dimension in range(alpha.shape[1]):
        question_results[f"alpha_{dimension + 1}"] = (
            alpha[:, dimension].detach().cpu().numpy()
        )
    question_results["d"] = d.detach().cpu().numpy()
    pd.DataFrame(question_results).to_csv(questions_path, index=False)

    print(f"\nSaved player results to {players_path}")
    print(f"Saved question results to {questions_path}")


def parse_args():
    """Define and read the command-line options accepted by this script."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--method", choices=("svi", "mcmc"), default="svi")
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA_PATH)
    parser.add_argument("--dimensions", type=int, default=2, help="latent skill dimensions")
    parser.add_argument("--steps", type=int, default=1000, help="SVI optimization steps")
    parser.add_argument("--lr", type=float, default=0.05, help="SVI learning rate")
    parser.add_argument("--num-samples", type=int, default=500, help="MCMC posterior samples")
    parser.add_argument("--warmup-steps", type=int, default=500, help="MCMC warmup steps")
    parser.add_argument("--num-chains", type=int, default=2, help="MCMC chains")
    parser.add_argument("--device", choices=("cpu", "cuda"), default="cuda")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    return parser.parse_args()


def main():
    """Run the complete load, train, summarize, and save process."""
    # Read the options supplied in the terminal.
    args = parse_args()

    # Stop early with a clear message if GPU training was requested but unavailable.
    if args.device == "cuda" and not torch.cuda.is_available():
        raise RuntimeError("CUDA requested, but no CUDA device is available")

    # Load the response data directly onto the selected CPU or GPU device.
    responses, mask, player_ids, question_ids = load_data(args.data, device=args.device)
    if args.dimensions < 1:
        raise ValueError("--dimensions must be at least 1")
    print(f"Device: {responses.device}")
    print(f"Players: {responses.shape[0]}  Questions: {responses.shape[1]}")
    print(f"Latent skill dimensions: {args.dimensions}")
    print(f"Observed cells: {mask.sum().item():,}  ({mask.float().mean():.1%} of matrix)\n")

    # Train with the method selected by --method.
    if args.method == "svi":
        fitted_model = train_svi(
            responses, mask, n_dimensions=args.dimensions, n_steps=args.steps, lr=args.lr
        )
    else:
        fitted_model = train_mcmc(
            responses,
            mask,
            n_dimensions=args.dimensions,
            num_samples=args.num_samples,
            warmup_steps=args.warmup_steps,
            num_chains=args.num_chains,
        )

    # Extract one final median estimate for every player and question parameter.
    posterior = posterior_median(fitted_model)
    theta = posterior["theta"]  # (n_players, n_dimensions)
    alpha = posterior["alpha"]  # (n_questions, n_dimensions)
    d = posterior["d"]  # (n_questions,)

    # Each latent dimension is reported separately because MIRT has no single
    # scalar player ability or question discrimination.
    for dimension in range(args.dimensions):
        print(
            f"\nTheta {dimension + 1} - mean: {theta[:, dimension].mean():.3f}  "
            f"std: {theta[:, dimension].std():.3f}"
        )
        print(
            f"Alpha {dimension + 1} - mean: {alpha[:, dimension].mean():.3f}  "
            f"std: {alpha[:, dimension].std():.3f}"
        )
    print(f"\nDifficulty d - mean: {d.mean():.3f}  std: {d.std():.3f}")

    # Save all player and question estimates.
    save_results(args.output_dir, player_ids, question_ids, theta, alpha, d)


# Python runs main() only when this file is executed directly. It does not run
# main() when another Python file imports something from train.py.
if __name__ == "__main__":
    main()
