import sys, os
import random   # >>> FIXED <<<
# Detect if running inside Jupyter
if "__file__" in globals():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
else:
    project_root = os.path.abspath(os.path.join(os.getcwd(), ".."))

sys.path.append(project_root)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

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


mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['ps.fonttype'] = 42
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
mpl.rcParams['mathtext.fontset'] = 'cm'
mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.size'] = 30


def print_mse_table(model_name, epsilon, phase1_pcts, means, n_total=200):
    print(f"\n================ MSE TABLE ({model_name} MODEL, ε = {epsilon}) ================\n")

    n1_values = [int(n_total * (p/100)) for p in phase1_pcts]
    headers = ["Phase 1"] + [f"n1={v}" for v in n1_values]

    rows = []
    rows.append(["RS+RFD"] + [f"{means['RS+RFD'][i]:.3e}" for i in range(len(phase1_pcts))])
    rows.append(["Corr-RR"] + [f"{means['Corr-RR'][i]:.3e}" for i in range(len(phase1_pcts))])

    col_widths = [
        max(len(row[i]) for row in rows + [headers]) + 2
        for i in range(len(headers))
    ]

    print("".join(headers[i].ljust(col_widths[i]) for i in range(len(headers))))
    print("-" * sum(col_widths))

    for row in rows:
        print("".join(row[i].ljust(col_widths[i]) for i in range(len(headers))))

    print()


# =================================================================
#                 STAR MODEL SWEEP (PRINT ONLY)
# =================================================================
def sweep_vs_phase1_star_table(
    phase1_pcts,
    epsilon,
    n,
    R,
    domain,
    rho,
    d,
    seed,
    x1_marginal=None,
    q_marginal=None,
    use_corr_rr=True,
):
    # Global seeding for dataset generation
    np.random.seed(seed)      # >>> FIXED <<<
    random.seed(seed)         # >>> FIXED <<<

    if x1_marginal is None:
        x1_marginal = {v: 1 / len(domain) for v in domain}

    df = gen_star_from_x1(
        n=n, domain=domain, d=d,
        x1_marginal=x1_marginal,
        rho=rho, q_marginal=q_marginal,
        seed=seed
    )

    true_freqs = get_true_frequencies(df)

    means = {
        "RS+RFD": np.zeros(len(phase1_pcts)),
        "Corr-RR": np.zeros(len(phase1_pcts)),
    }

    for idx, pct in enumerate(phase1_pcts):
        frac = pct / 100

        for r in range(R):
            # Re-seed for deterministic perturbation
            np.random.seed(seed + idx*1000 + r)  # >>> FIXED <<<
            random.seed(seed + idx*1000 + r)     # >>> FIXED <<<

            # === RS+RFD ===
            est_I1, df_B1, dom1 = corr_rr_phase1_spl(df, epsilon, frac=frac)
            n1 = len(df) - len(df_B1)
            n2 = len(df_B1)

            pert_fd = rs_rfd_perturb(df_B1, dom1, est_I1, epsilon)
            est_II = rs_rfd_estimate(pert_fd, dom1, est_I1, epsilon)
            comb_fd = combine_phase_estimates(est_I1, est_II, n1, n2)

            means["RS+RFD"][idx] += np.mean([compute_mse(true_freqs[c], comb_fd[c]) for c in df.columns])

            # === Corr-RR ===
            if use_corr_rr:
                est_I2, df_B2, dom2 = corr_rr_phase1_spl(df, epsilon, frac=frac)
                n1c = len(df) - len(df_B2)
                n2c = len(df_B2)

                p_y = build_p_y_table(est_I2, n2c, dom2, epsilon)

                pert_corr = corr_rr_phase2_perturb(df_B2, epsilon, est_I2, dom2, p_y)
                est_IIc = corr_rr_estimate(pert_corr, dom2, epsilon)

                comb_rr = combine_phase_estimates(est_I2, est_IIc, n1c, n2c)

                means["Corr-RR"][idx] += np.mean([compute_mse(true_freqs[c], comb_rr[c]) for c in df.columns])

        means["RS+RFD"][idx] /= R
        means["Corr-RR"][idx] /= R

    return means


# =================================================================
#           PROGRESSIVE MODEL SWEEP (PRINT ONLY)
# =================================================================
def sweep_vs_phase1_progressive_table(
    phase1_pcts,
    epsilon,
    n,
    R,
    domain,
    rho,
    d,
    seed,
    x1_marginal=None,
    q_marginal=None,
    use_corr_rr=True,
):
    # Global seeding
    np.random.seed(seed)      # >>> FIXED <<<
    random.seed(seed)         # >>> FIXED <<<

    if x1_marginal is None:
        x1_marginal = {v: 1 / len(domain) for v in domain}

    df = gen_progressive(
        n=n, domain=domain, d=d,
        x1_marginal=x1_marginal,
        rho=rho, q_marginal=q_marginal,
        seed=seed
    )

    true_freqs = get_true_frequencies(df)

    means = {
        "RS+RFD": np.zeros(len(phase1_pcts)),
        "Corr-RR": np.zeros(len(phase1_pcts)),
    }

    for idx, pct in enumerate(phase1_pcts):
        frac = pct / 100

        for r in range(R):
            # Re-seed inside loop
            np.random.seed(seed + idx*1000 + r)  # >>> FIXED <<<
            random.seed(seed + idx*1000 + r)     # >>> FIXED <<<

            # RS+RFD
            est_I1, df_B1, dom1 = corr_rr_phase1_spl(df, epsilon, frac=frac)
            n1 = len(df) - len(df_B1)
            n2 = len(df_B1)

            pert_fd = rs_rfd_perturb(df_B1, dom1, est_I1, epsilon)
            est_II = rs_rfd_estimate(pert_fd, dom1, est_I1, epsilon)
            comb_fd = combine_phase_estimates(est_I1, est_II, n1, n2)

            means["RS+RFD"][idx] += np.mean([compute_mse(true_freqs[c], comb_fd[c]) for c in df.columns])

            # Corr-RR
            if use_corr_rr:
                est_I2, df_B2, dom2 = corr_rr_phase1_spl(df, epsilon, frac=frac)
                n1c = len(df) - len(df_B2)
                n2c = len(df_B2)

                p_y = build_p_y_table(est_I2, n2c, dom2, epsilon)

                pert_corr = corr_rr_phase2_perturb(df_B2, epsilon, est_I2, dom2, p_y)
                est_IIc = corr_rr_estimate(pert_corr, dom2, epsilon)

                comb_rr = combine_phase_estimates(est_I2, est_IIc, n1c, n2c)

                means["Corr-RR"][idx] += np.mean([compute_mse(true_freqs[c], comb_rr[c]) for c in df.columns])

        means["RS+RFD"][idx] /= R
        means["Corr-RR"][idx] /= R

    return means



# =================================================================
#           TOP-LEVEL EXPERIMENT DRIVER
# =================================================================
def run_phase1_experiment(
    model="STAR",
    epsilons=[0.1, 0.3, 0.5],
    phase1_pcts=[5,10,15,20,25,30,35,40,45,50],
    n=200,
    domain=[0,1,2,3],
    R=50,
    rho=0.9,
    d=2,
    seed=42,
    x1_marginal=None,
):

    # Global deterministic seed once
    np.random.seed(seed)      # >>> FIXED <<<
    random.seed(seed)         # >>> FIXED <<<
    
    for epsilon in epsilons:

        if model == "STAR":
            means = sweep_vs_phase1_star_table(
                phase1_pcts=phase1_pcts,
                epsilon=epsilon,
                n=n,
                R=R,
                domain=domain,
                rho=rho,
                d=d,
                seed=seed
            )

        else:
            means = sweep_vs_phase1_progressive_table(
                phase1_pcts=phase1_pcts,
                epsilon=epsilon,
                n=n,
                R=R,
                domain=domain,
                rho=rho,
                d=d,
                seed=seed
            )

        print_mse_table(model, epsilon, phase1_pcts, means, n_total=n)


if __name__ == "__main__":

    # ------------------------------
    # Common experiment settings
    # ------------------------------
    epsilons = [0.1, 0.3, 0.5]          # ε values to test
    phase1_pcts = [5,10,15,20,25,30,35,40,45,50]
    n = 20000
    domain = [0,1,2,3]
    rho = 0.1
    d = 2
    R = 100                              # use R=50 for real experiment
    seed = 42
    x1_marginal = {0: 0.4, 1: 0.3, 2: 0.2, 3: 0.1}
    run_phase1_experiment(
        model="PROGRESSIVE",
        epsilons=epsilons,
        phase1_pcts=phase1_pcts,
        n=n,
        domain=domain,
        R=R,
        rho=rho,
        d=d,
        seed=seed,
        x1_marginal = x1_marginal,
    )


