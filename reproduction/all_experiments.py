import subprocess
import sys
import os
from pathlib import Path

# Paths
ROOT_DIR = Path(__file__).resolve().parent.parent
REPRO_DIR = ROOT_DIR / "reproduction"
OUT_DIR = ROOT_DIR / "generated_results"

OUT_DIR.mkdir(exist_ok=True)

# scripts = [
#     "fig_2.py",
#     "fig_3a.py",
#     "fig_3b.py",
#     "fig_3c.py",
#     "fig_4a.py",
#     "fig_4b.py",
#     "fig_4c.py",
#     "fig_5a.py",
#     "fig_5b.py",
#     "fig_5c.py",
#     "fig_6a.py",
#     "fig_6b.py",
#     "fig_6c.py",
#     "fig_7a.py",
#     "fig_7b.py",
#     "fig_7c.py",
#     "fig_8a.py",
#     "fig_8b.py",
#     "fig_8c.py",
#     "fig_9a.py",
#     "fig_9b.py",
#     "fig_9c.py",
#     "fig_10a.py",
#     "fig_10b.py",
#     "fig_10c.py",
#     "fig_11a.py",
#     "fig_11b.py",
#     "fig_11c.py",
#     "fig_12a.py",
#     "fig_12b.py",
#     "fig_12c.py",
#     "fig_13a.py",
#     "fig_13b.py",
#     "fig_13c.py",
#     "fig_14a.py",
#     "fig_14b.py",
#     "fig_14c.py",
#     "table_2.py",
#     "table_3.py",
#     "table_4.py",
#     "table_5.py",
#     "table_6.py",
#     "table_7.py",
#     "table_8.py",
#     "table_9.py",
# ]

scripts = [
    "fig_11a.py",
    "fig_11b.py",
    "fig_11c.py",
]


for script in scripts:
    env = os.environ.copy()

    env["MPLBACKEND"] = "Agg"

    env["FIG_OUT_DIR"] = str(OUT_DIR)

    subprocess.run(
        [sys.executable, str(REPRO_DIR / script)],
        env=env,
        check=True,
    )

print(f"\nAll figures saved in: {OUT_DIR}\n")
