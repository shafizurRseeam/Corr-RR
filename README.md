[![arXiv](https://img.shields.io/badge/arXiv-2507.17516-b31b1b.svg)](https://arxiv.org/abs/2507.17516) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository contains the official implementation and reproducibility package for the paper:

“Frequency Estimation of Correlated Multi-attribute Data under Local Differential Privacy” (PETS'26)


**📘Contributions:** 

* This paper proposes a two-phase LDP Framework, Correlated Randomized Response (Corr-RR), for Multi-attribute Correlated Data.
* Corr-RR leverages inter-intributes correlations to derive correlation-aware parameter $p_y$ privately in Phase I, which guides Phase II perturbation, and overall improves the frequency estiamtion.
* Results indicate that with higher correlation and higher number attributes, Corr-RR performs significantly better than baselines.  


![img.png](Figures/fig_1.png)

---
## 📁 Repository Structure 
The main folders and files are as follows:

```
|- Figures (Figures used in the paper)
|- experiments_notebook (All experiments in Jupyter notebooks)
|- preprocessed_data (Preprocessed real-world datasets (Clave, Mushroom, Adults))
|- reproduction (Scripts to reproduce all results in the paper)
|- utils (Utility functions for Corr-RR and baselines)
|- ...
```

## 🔁 Reproduction 

📥 Clone the Repository
```bash
git clone https://github.com/shafizurRseeam/Corr-RR.git
cd Corr-RR
```
### ⚙️ Installation
Tested environments: `uv` version `0.9.16` and Python version `3.11`~`3.12`.

**Install UV package manager.**
This project is packaged by `uv`, a modern Python package management system similar to `miniconda` or `poetry`.
All dependencies are listed in `pyproject.toml`.
We recommend using `uv` to create a virtual environment and install the dependencies.


To install `uv`, follow the instructions in the "[uv installation](https://docs.astral.sh/uv/)". Below are quick-install commands.


**Windows (PowerShell)**

```bash
PS> powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
**macOS / Linux**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

After installation, ensure that `uv` is added to your system PATH. Verify installation:

```
uv --version
```

**Install dependencies.**
Navigate to the project root and run:

```
[PROJECT_ROOT]$ uv sync
```
This command creates a virtual environment in the project root and installs the dependencies listed in `pyproject.toml`.

## ▶️ Running Experiments
### Option 1 (Recommended) - Using `uv`
The `reproduction` folder contains scripts for reproducing all figures and tables.

```
|- reproduction
  |- fig_2.py: Figure 2 (<1 Sec)
  |- fig_3a.py: Figure 3a  (<28 minute)
  |- table_2.py: Table 2  (<1 sec)
  |- ...

```

You can run these scripts directly with `uv run` (no need to manually activate the environment) to generate Figures and Tables. Run any script using:
```
[PROJECT_ROOT]$ uv run ./reproduction/fig_3a.py
```
This will generate the figure using matplotlib or print the table in the terminal.
Results should match those in the paper (minor randomness expected).

**⏱️Approximate Runtimes (Rounded)**


| Figure Group                                              | Windows (Xeon W-2145, 32 GB RAM) | macOS (M2 Pro, 16 GB RAM) |
|-----------------------------------------------------------|-----------------------------------|----------------------------|
| **Fig 2**                                                 | ~2 sec                               | ~1 sec                        |
| **Fig 3 (a,b,c), Fig 4 (a,b,c)**                          | ~75 min                            | ~28 min                     |
| **Fig 5 (a,b,c), Fig 6 (a,b,c), Fig 13 (a,b,c), Fig 14(a,b,c)**  | ~80 min                            | ~30 min                     |
| **Fig 7 (a,b,c), Fig 8 (a,b,c)**                          | —                                 | ~75 min                     |
| **Fig 9 (a,b,c), Fig 10 (a,b,c)**                         | ~45 min                            | ~15 min                     |
| **Fig 11 (a,b,c)**                                        | ~18min / ~14min / ~23min                   | —                          |
| **Fig 12 (a,b,c)**                                        | ~3 sec                               | ~1 sec                        |
| **Table 2**                                               | ~1 sec                               | ~2 sec                        |
| **Table 3**                                               | ~1 sec                               | ~1 sec                        |
| **Tables 4 & 7**                                          | ~3 min                             | ~25 sec                       |
| **Tables 5 & 8**                                          | ~13 min                            | ~4 min                      |
| **Tables 6 & 9**                                          | ~75 min                             | ~30 min                     |


### Option 2 — Jupyter Notebooks

The `experiments_notebook` folder contains self-contained Jupyter notebooks for interactive exploration: 

```
|- experiments_notebook
  |- misc.ipynb
  |- MSE_vs_Attribute.ipynb
  |- MSE_vs_Budget.ipynb
  |- ........

```
Users can modify parameters to explore different experimental settings.




