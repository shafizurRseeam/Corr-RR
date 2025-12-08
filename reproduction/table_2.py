import sys, os





# Detect if running inside Jupyter
if "__file__" in globals():
    # Running as a .py script
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
else:
    # Running inside Jupyter Notebook
    # Assume notebook is inside project/reproduction/
    project_root = os.path.abspath(os.path.join(os.getcwd(), ".."))

sys.path.append(project_root)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import os

from utils.data_utils_newest import gen_star_from_x1, get_true_frequencies, gen_progressive
from utils.metrics import compute_mse
from utils.spl import random_split_perturb, random_split_estimate
from utils.rs_fd import rs_fd_perturb, rs_fd_estimate
from utils.rs_rfd import rs_rfd_perturb, rs_rfd_estimate
from utils.corr_rr_fixed_new import (
    corr_rr_phase1_spl,
    corr_rr_phase2_perturb,
    corr_rr_estimate,
    combine_phase_estimates,
    optimal_p_y,
    build_p_y_table,
)


mpl.rcParams['pdf.fonttype'] = 42   # TrueType
mpl.rcParams['ps.fonttype'] = 42    # TrueType for EPS


mpl.rc('font', family='DejaVu Serif')


mpl.rcParams.update({
    'text.usetex': False,
    'font.size': 16,
    'axes.titlesize': 20,
    'axes.labelsize': 20,
    'xtick.labelsize': 20,
    'ytick.labelsize': 20,
    'legend.fontsize': 20,
    'figure.titlesize': 20,
})
mpl.rcParams['mathtext.fontset'] = 'cm'     # Math font
mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.size'] = 30
# ---------------- helpers ----------------
def _normalize_dist(d):
    vals = np.array([max(0.0, float(v)) for v in d.values()], dtype=float)
    s = vals.sum()
    if s <= 0:
        k = len(vals)
        vals = np.full(k, 1.0 / k)
    else:
        vals = vals / s
    return {k: vals[i] for i, k in enumerate(d.keys())}



def _build_p_y_table_minimal(est_I, epsilon, n2, domain, cols):
    return {
        (a, b): float(optimal_p_y(est_I[a], est_I[b], epsilon, n2, domain))
        for a in cols for b in cols if a != b
    }
import numpy as np
import pandas as pd

def compute_pairwise_correlations(df):
    """Return list of ((Xi, Xj), corr) sorted by pair."""
    corr = df.astype(float).corr()
    cols = df.columns
    pairs = []
    for i in range(len(cols)):
        for j in range(i+1, len(cols)):
            pairs.append(((cols[i], cols[j]), corr.iloc[i, j]))
    return pairs


def correlation_table_syna_synb(
    rhos=(0.1, 0.5, 0.9),
    n=20000,
    domain=[0,1,2,3],
    d=4,
    seed=42,
    x1_marginal=None,
    q_marginal=None,
):
    """
    Computes pairwise Pearson correlations for:
      - SynA (STAR model)
      - SynB (Progressive model)
    across multiple rho values.

    Prints in a clean table form.
    """

    if x1_marginal is None:
        x1_marginal = {v: 1.0/len(domain) for v in domain}

    if seed is not None:
        np.random.seed(seed)

    # To preserve column ordering
    colnames = [f"X{i+1}" for i in range(d)]

    # Storage: { pair: [SynA_rho1, SynB_rho1, SynA_rho2, SynB_rho2, ...]}
    results = {}

    for rho in rhos:

        # ======== Generate SynA (Star model) ========
        df_star = gen_star_from_x1(
            n=n,
            domain=domain,
            d=d,
            x1_marginal=x1_marginal,
            rho=rho,
            q_marginal=q_marginal,
            seed=seed,
        )
        df_star.columns = colnames
        star_pairs = compute_pairwise_correlations(df_star)

        # ======== Generate SynB (Progressive model) ========
        df_prog = gen_progressive(
            n=n,
            domain=domain,
            d=d,
            x1_marginal=x1_marginal,
            rho=rho,
            q_marginal=q_marginal,
            seed=seed,
        )
        df_prog.columns = colnames
        prog_pairs = compute_pairwise_correlations(df_prog)

        # Store results
        for ((x_i, x_j), corr_a), (_, corr_b) in zip(star_pairs, prog_pairs):
            key = (x_i, x_j)
            if key not in results:
                results[key] = []
            results[key].extend([corr_a, corr_b])

    # =========================
    # Print formatted table
    # =========================
    header = ["Pair"]
    for rho in rhos:
        header += [f"SynA(rho={rho})", f"SynB(rho={rho})"]

    # Determine widths
    col_widths = [max(len(h), 12) for h in header]

    # Print header
    line = "".join(h.ljust(col_widths[i]) for i, h in enumerate(header))
    print("\n" + line)
    print("-" * len(line))

    # Print rows
    averages = np.zeros(len(rhos) * 2)

    for pair, vals in results.items():
        row = [f"({pair[0]}, {pair[1]})"] + [f"{v:.3f}" for v in vals]
        for i, cell in enumerate(row):
            print(cell.ljust(col_widths[i]), end="")
        print()

        averages += np.array(vals)

    # Average row
    avg_vals = averages / len(results)
    avg_row = ["Average"] + [f"{v:.3f}" for v in avg_vals]
    for i, cell in enumerate(avg_row):
        print(cell.ljust(col_widths[i]), end="")

    print("\n")
if __name__ == "__main__":
    correlation_table_syna_synb(
        rhos=[0.1, 0.5, 0.9],
        n=20000,
        domain=[0,1,2,3],
        d=4,
        seed=42
    )
