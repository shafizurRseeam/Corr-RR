import sys, os
import os
from pathlib import Path




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

import numpy as np
import matplotlib.pyplot as plt
from typing import List, Dict, Optional, Sequence, Union

def plot_grouped_value_distribution(
    df: pd.DataFrame,
    cols: Sequence[str],
    *,
    normalize: bool = True,                 # True => relative frequency; False => raw counts
    x_label: str = "Attribute Value",
    y_label: str = "Rel. Frequency",
    title: Optional[str] = None,
    figsize: tuple = (6, 4),
    palette: Optional[Sequence[str]] = None,
    bar_edgecolor: str = "black",
    bar_alpha: float = 1.0,
    bar_gap: float = 0.8,
    label_rotation: int = 0,
    font_sizes: Dict[str, Union[int, float]] = None,  # {"axes": 20, "ticks": 18, "legend": 18, "xticks": 22}
    save_path: Optional[str] = None,
    dpi: int = 300,
    tight_layout: bool = True
):
    """
    Draw grouped bars for the value distribution of multiple attributes (cols).
    Works for discrete/integer-like columns (categorical codes or small integer domains).
    """

    # Default font sizes
    if font_sizes is None:
        font_sizes = {"title": 13, "axes": 11, "ticks": 9, "legend": 10, "xticks": 12}

    # Build shared domain
    domains = [set(df[c].dropna().unique()) for c in cols]
    x_values = sorted(set().union(*domains))
    x_positions = np.arange(len(x_values))

    # Compute frequencies
    series_list = []
    for c in cols:
        vc = df[c].value_counts(normalize=normalize).sort_index()
        series_list.append(vc.reindex(x_values, fill_value=0))

    fig, ax = plt.subplots(figsize=figsize)

    # Colors
    if palette is None:
        palette = [None] * len(cols)
    elif len(palette) < len(cols):
        repeats = int(np.ceil(len(cols) / len(palette)))
        palette = (list(palette) * repeats)[:len(cols)]

    # Bar geometry
    group_width = min(max(bar_gap, 0.2), 0.95)
    bar_width = group_width / len(cols)

    for i, (c, s) in enumerate(zip(cols, series_list)):
        offsets = x_positions + (i - (len(cols) - 1) / 2) * bar_width

        # Convert column name "X1" -> "$X_1$"
        if c.startswith("X") and c[1:].isdigit():
            legend_label = f"$X_{{{c[1:]}}}$"
        else:
            legend_label = c  # keep original

        ax.bar(
            offsets,
            s.values,
            width=bar_width,
            label=legend_label,
            edgecolor=bar_edgecolor,
            alpha=bar_alpha,
            color=palette[i]
        )

    # Labels
    ax.set_xlabel(x_label, fontsize=font_sizes["axes"])
    ax.set_ylabel(y_label if normalize else "Frequency", fontsize=font_sizes["axes"])

    # X-axis tick labels with BIGGER font
    ax.set_xticks(x_positions)
    ax.set_xticklabels(x_values, rotation=label_rotation, fontsize=font_sizes.get("xticks", 16))

    # Y ticks
    ax.tick_params(axis='y', labelsize=font_sizes["ticks"])

    # Legend
    leg = ax.legend(fontsize=font_sizes["legend"])
    if leg:
        leg.set_title(None)

    if normalize:
        ax.set_ylim(0, 1.0)

    if tight_layout:
        plt.tight_layout()

    out_dir = os.environ.get("FIG_OUT_DIR")

    if save_path is not None:
    # Explicit save path (manual use)
        plt.savefig(save_path, dpi=dpi, bbox_inches="tight")
        print(f"Saved figure to: {save_path}")

    elif out_dir is not None:
    # Automation: save to generated_figures/
        Path(out_dir).mkdir(parents=True, exist_ok=True)
        fname = Path(__file__).stem + ".pdf"
        save_path = Path(out_dir) / fname
        plt.savefig(save_path, dpi=dpi, bbox_inches="tight")
        print(f"Saved figure to: {save_path}")
    plt.show()




if "__file__" in globals():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
else:
    project_root = os.path.abspath(os.path.join(os.getcwd(), ".."))

data_path = os.path.join(project_root, "preprocessed_data", "mushroom.csv")

df_m = pd.read_csv(data_path)


plot_grouped_value_distribution(
    df_m,
    cols=["X1", "X2"],        # will automatically convert to X_1, X_2, X_3
    normalize=True,
    x_label="Attribute Value",
    y_label="Rel. Frequency",
    figsize=(8,6),
    palette=["#4C78A8", "#F58518", "#54A24B"],
    bar_edgecolor="black",
    bar_alpha=1.0,
    font_sizes={"axes": 30, "ticks": 20, "legend": 25, "xticks": 25},
    #save_path=r"C:\\Users\\ss6365\\Desktop\\Corr-RR\\fig\fig_12b.pdf",
)