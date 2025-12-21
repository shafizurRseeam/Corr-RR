import sys, os
import random
from pathlib import Path

# -------------------------------------------------------------
# Detect project root
# -------------------------------------------------------------
if "__file__" in globals():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
else:
    project_root = os.path.abspath(os.path.join(os.getcwd(), ".."))

sys.path.append(project_root)

import numpy as np
import pandas as pd

from utils.data_utils_newest import gen_star_from_x1, get_true_frequencies, gen_progressive
from utils.metrics import compute_mse
from utils.rs_rfd import rs_rfd_perturb, rs_rfd_estimate
from utils.corr_rr_fixed_new import (
    corr_rr_phase1_spl,
    corr_rr_phase2_perturb,
    corr_rr_estimate,
    combine_phase_estimates,
    build_p_y_table,
)

# =============================================================
# Pretty printer (terminal only)
# =============================================================
def print_mse_table(model_name, epsilon, phase1_pcts, means, n_total):
    print(f"\n================ MSE TABLE ({model_name} MODEL, ε = {epsilon}) ================\n")

    n1_values = [int(n_total * (p / 100)) for p in phase1_pcts]
    headers = ["Phase 1"] + [f"n1={v}" for v in n1_values]

    rows = [
        ["RS+RFD"] + [f"{means['RS+RFD'][i]:.3e}" for i in range(len(phase1_pcts))],
        ["Corr-RR"] + [f"{means['Corr-RR'][i]:.3e}" for i in range(len(phase1_pcts))],
    ]

    col_widths = [
        max(len(row[i]) for row in rows + [headers]) + 2
        for i in range(len(headers))
    ]

    print("".join(headers[i].ljust(col_widths[i]) for i in range(len(headers))))
    print("-" * sum(col_widths))
    for row in rows:
        print("".join(row[i].ljust(col_widths[i]) for i in range(len(headers))))
    print()


# =============================================================
# STAR MODEL
# =============================================================
def sweep_star(phase1_pcts, epsilon, n, R, domain, rho, d, seed, x1_marginal):
    np.random.seed(seed)
    random.seed(seed)

    df = gen_star_from_x1(
        n=n, domain=domain, d=d,
        x1_marginal=x1_marginal,
        rho=rho, seed=seed
    )

    true_freqs = get_true_frequencies(df)

    means = {
        "RS+RFD": np.zeros(len(phase1_pcts)),
        "Corr-RR": np.zeros(len(phase1_pcts)),
    }

    for i, pct in enumerate(phase1_pcts):
        frac = pct / 100

        for r in range(R):
            np.random.seed(seed + i * 1000 + r)
            random.seed(seed + i * 1000 + r)

            # RS+RFD
            est_I, df_B, dom = corr_rr_phase1_spl(df, epsilon, frac=frac)
            n1 = len(df) - len(df_B)
            n2 = len(df_B)

            pert = rs_rfd_perturb(df_B, dom, est_I, epsilon)
            est_II = rs_rfd_estimate(pert, dom, est_I, epsilon)
            comb = combine_phase_estimates(est_I, est_II, n1, n2)

            means["RS+RFD"][i] += np.mean([
                compute_mse(true_freqs[c], comb[c]) for c in df.columns
            ])

            # Corr-RR
            est_I2, df_B2, dom2 = corr_rr_phase1_spl(df, epsilon, frac=frac)
            n1c = len(df) - len(df_B2)
            n2c = len(df_B2)

            p_y = build_p_y_table(est_I2, n2c, dom2, epsilon)
            pert_corr = corr_rr_phase2_perturb(df_B2, epsilon, est_I2, dom2, p_y)
            est_IIc = corr_rr_estimate(pert_corr, dom2, epsilon)
            comb_rr = combine_phase_estimates(est_I2, est_IIc, n1c, n2c)

            means["Corr-RR"][i] += np.mean([
                compute_mse(true_freqs[c], comb_rr[c]) for c in df.columns
            ])

        means["RS+RFD"][i] /= R
        means["Corr-RR"][i] /= R

    return means


# =============================================================
# PROGRESSIVE MODEL
# =============================================================
def sweep_progressive(phase1_pcts, epsilon, n, R, domain, rho, d, seed, x1_marginal):
    np.random.seed(seed)
    random.seed(seed)

    df = gen_progressive(
        n=n, domain=domain, d=d,
        x1_marginal=x1_marginal,
        rho=rho, seed=seed
    )

    true_freqs = get_true_frequencies(df)

    means = {
        "RS+RFD": np.zeros(len(phase1_pcts)),
        "Corr-RR": np.zeros(len(phase1_pcts)),
    }

    for i, pct in enumerate(phase1_pcts):
        frac = pct / 100

        for r in range(R):
            np.random.seed(seed + i * 1000 + r)
            random.seed(seed + i * 1000 + r)

            est_I, df_B, dom = corr_rr_phase1_spl(df, epsilon, frac=frac)
            n1 = len(df) - len(df_B)
            n2 = len(df_B)

            pert = rs_rfd_perturb(df_B, dom, est_I, epsilon)
            est_II = rs_rfd_estimate(pert, dom, est_I, epsilon)
            comb = combine_phase_estimates(est_I, est_II, n1, n2)

            means["RS+RFD"][i] += np.mean([
                compute_mse(true_freqs[c], comb[c]) for c in df.columns
            ])

            est_I2, df_B2, dom2 = corr_rr_phase1_spl(df, epsilon, frac=frac)
            n1c = len(df) - len(df_B2)
            n2c = len(df_B2)

            p_y = build_p_y_table(est_I2, n2c, dom2, epsilon)
            pert_corr = corr_rr_phase2_perturb(df_B2, epsilon, est_I2, dom2, p_y)
            est_IIc = corr_rr_estimate(pert_corr, dom2, epsilon)
            comb_rr = combine_phase_estimates(est_I2, est_IIc, n1c, n2c)

            means["Corr-RR"][i] += np.mean([
                compute_mse(true_freqs[c], comb_rr[c]) for c in df.columns
            ])

        means["RS+RFD"][i] /= R
        means["Corr-RR"][i] /= R

    return means


# =============================================================
# MAIN DRIVER (ONE CSV PER MODEL)
# =============================================================
def run_phase1_experiment(
    model,
    epsilons,
    phase1_pcts,
    n,
    domain,
    R,
    rho,
    d,
    seed,
    x1_marginal,
):
    all_rows = []

    for epsilon in epsilons:
        if model == "STAR":
            means = sweep_star(
                phase1_pcts, epsilon, n, R, domain, rho, d, seed, x1_marginal
            )
        else:
            means = sweep_progressive(
                phase1_pcts, epsilon, n, R, domain, rho, d, seed, x1_marginal
            )

        print_mse_table(model, epsilon, phase1_pcts, means, n)

        n1_vals = [int(n * (p / 100)) for p in phase1_pcts]
        for i, pct in enumerate(phase1_pcts):
            all_rows.append({
                "model": model,
                "epsilon": epsilon,
                "Phase1_pct": pct,
                "n1": n1_vals[i],
                "RS+RFD": means["RS+RFD"][i],
                "Corr-RR": means["Corr-RR"][i],
            })

    out_dir = os.environ.get("FIG_OUT_DIR")
    if out_dir:
        Path(out_dir).mkdir(parents=True, exist_ok=True)
        pd.DataFrame(all_rows).to_csv(
            Path(out_dir) / f"table_5.csv",
            index=False
        )


# =============================================================
# ENTRY POINT
# =============================================================
if __name__ == "__main__":
    run_phase1_experiment(
        model="STAR",
        epsilons=[0.1, 0.3, 0.5],
        phase1_pcts=[5,10,15,20,25,30,35,40,45,50],
        n=2000,
        domain=[0,1,2,3],
        R=100,
        rho=0.1,
        d=2,
        seed=42,
        x1_marginal={0:0.4,1:0.3,2:0.2,3:0.1},
    )

    # run_phase1_experiment(
    #     model="PROGRESSIVE",
    #     epsilons=[0.1, 0.3, 0.5],
    #     phase1_pcts=[5,10,15,20,25,30,35,40,45,50],
    #     n=200,
    #     domain=[0,1,2,3],
    #     R=100,
    #     rho=0.1,
    #     d=2,
    #     seed=42,
    #     x1_marginal={0:0.4,1:0.3,2:0.2,3:0.1},
    # )
