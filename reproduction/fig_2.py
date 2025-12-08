import numpy as np
import matplotlib.pyplot as plt

# ==========================================================
# Function to compute optimal p_y
# ==========================================================
def optimal_p_y(f_a, f_b, epsilon, n, domain):
    d = len(domain)
    exp_eps = np.exp(epsilon)
    p = exp_eps / (exp_eps + d - 1)
    q = 1.0 / (exp_eps + d - 1)
    Δ = p - q

    S1 = d * (d - 1) / 2
    S2 = (d - 1) * d * (2 * d - 1) / 6

    μa = sum(v * f_a[v] for v in domain)
    μb = sum(v * f_b[v] for v in domain)
    νb2 = sum(v**2 * f_b[v] for v in domain)

    a0 = μa - μb
    a1 = 2 * μb - S1
    b1 = 2 * νb2 - S2
    Y0 = (Δ / 2) * a0 + (S1 / 2)

    α1 = 2 * sum((1 - f_a[v] - f_b[v]) * ((2 * f_a[v] - 1) + (2 * f_b[v] - 1)) for v in domain)
    α2 = sum((2 * f_a[v] - 1)**2 + (2 * f_b[v] - 1)**2 for v in domain)

    num = (b1 - 2 * Y0 * a1) / (2 * n * Δ) + α1 / (8 * d)
    den = a1**2 / (2 * n) - α2 / (4 * d)

    p_star = num / den if den != 0 else q
    return float(np.clip(p_star, 0.0, 1.0))


# ==========================================================
# MAIN: Run the p_y plot experiment
# ==========================================================
if __name__ == "__main__":

    # --- constants ---
    domain = [0, 1]       # Binary domain
    epsilon = 0.1
    n = 1000

    # --- f_a curves to plot ---
    fa_fixed_values = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    colors = plt.cm.plasma(np.linspace(0.15, 0.85, len(fa_fixed_values)))
    fb_values = np.linspace(0, 1, 400)

    # --- figure ---
    plt.figure(figsize=(7, 5))

    for fa_val, color in zip(fa_fixed_values, colors):
        py_values = []
        for fb_val in fb_values:
            f_a = {0: fa_val, 1: 1 - fa_val}
            f_b = {0: fb_val, 1: 1 - fb_val}
            py_values.append(optimal_p_y(f_a, f_b, epsilon, n, domain))

        label = rf'$\hat{{f}}^I_s = {fa_val}$'
        plt.plot(fb_values, py_values, color=color, linewidth=2, label=label)

    # --- quadrant lines ---
    plt.axvline(0.5, color="gray", linestyle="--", linewidth=0.8, alpha=0.6)
    plt.axhline(0.5, color="gray", linestyle="--", linewidth=0.8, alpha=0.6)

    # --- axis ---
    plt.xlabel(r'$\hat{f}^I_j$', fontsize=24)
    plt.ylabel(r'$p_y$', fontsize=24)

    plt.xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0], fontsize=16)
    plt.yticks(fontsize=16)
    plt.ylim(-0.05, 1.05)

    # --- legend ---
    plt.legend(fontsize=21, loc='center left',
               bbox_to_anchor=(1.02, 0.5),
               frameon=True, edgecolor='black')

    plt.tight_layout()
    plt.show()

  