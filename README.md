[![arXiv](https://img.shields.io/badge/arXiv-2505.15483-<COLOR>.svg)](https://arxiv.org/abs/2505.15483)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[PETS'26] Frequency Estimation of Correlated Multi-attribute Data under Local Differential Privacy
 

**Contributions:** 

* This paper proposes a two-phase LDP Framework, Correlated Randomized Response (Corr-RR), for Multi-attribute Correlated Data.
* Corr-RR leverages inter-intributes correlations to derive correlation-aware parameter $p_y$ privately in Phase~I, which guides Phase~II perturbatio, and overall improves the frequency estiamtion. 

---

The main folders and files are as follows:

```
|- experiments_notebook (All experiments in Jupyter notebook. Parameters could be changed to see experiments on different settings)
|- Figures (All the figures used in the paper)
|- preprocessed_data (Pre-processed real-world datasets: Clave, Mushroom, Adults)
|- reproduction (Reproduction of the results in the paper)
|- utils (All required fuctions to run the experiments)
```

## Reproduction 

Tested environments: `uv` version `0.9.16` and Python version `3.12`~`3.13`.

**Install UV package manager.**
This project is packaged by `uv`, a modern Python package management system similar to `miniconda` or `poetry`.
All dependencies are listed in `pyproject.toml`.
We recommend using `uv` to create a virtual environment and install the dependencies.


To install `uv`, follow the instructions in the "[uv installation](https://docs.astral.sh/uv/)".

Here is a quick guide to install it in windows using powershell. 


**Quick guide to install in Windows using Powershell.**

```bash
PS> powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
**Quick guide to install in macOS and Linux using Terminal.**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

After installation, follow the prompts to add `uv` to your system's `PATH`.
You can verify the installation by running the following command in your terminal (Windows, Linux, or macOS):

```
uv --version
```
This should display the installed version of `uv`.

**Install dependencies.**
After installing `uv`, cd to the project root directory and run:

```
[PROJECT_ROOT]$ uv sync
```
This command creates a virtual environment in the project root and installs the dependencies listed in `pyproject.toml`.
You can then run the provided scripts to reproduce the results in the paper. Two options are available:

### Option 1 (Quick) -- Recommended

The `reproduction` folder contains scripts  to reproduce key results from the paper. The structure is as follows:

```
|- reproduction
  |- fig_2.py: Figure 2 (<1 Sec)
  |- figure_3a.py: Figure 12a  (<28 minute)
  |- table_2.py: Table 2 (Page 11~12)  (<1 sec)
  |- ........

```

You can run these scripts directly with `uv run` (no need to manually activate the environment) to generate Figures and Tables:
```
[PROJECT_ROOT]$ uv run ./reproduction/fig_3a.py
```
This will display the corresponding figures using matplotlib, and the tables in terminal. All the figures and results should be printed as it is in the main paper, with some varioation due to the stochastic nature of the experiments.

**Following in the runtime comparison (Approximate runtimes; values rounded for readability.)**


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


### Option 2 (Detailed)

The `experiments_notebook` folder contains jupyter notebook which is self contained. Interested ones can changes the parameters to see the results for different setting. 

```
|- experiments_notebook
  |- misc.ipynb
  |- MSE_vs_Attribute.ipynb
  |- MSE_vs_Budget.ipynb
  |- ........

```
## Example Python Code

```python
def hello():
    print("Hello, Seeam!")
```

---

## Example Bash Commands

```bash
git clone https://github.com/yourname/repo.git
cd repo
pip install -r requirements.txt
```

---





## Placeholder Sections (You can fill later)

### 📘 Introduction
(Add a short overview of the Corr-RR mechanism and goals.)

### ⚙️ Installation
(Explain how to install dependencies or set up environment.)

### ▶️ Running Experiments
(Show commands like: `python reproduction/fig_2.py`)

### 📁 Project Structure
(Brief explanation of folders: reproduction/, src/, data/, etc.)

