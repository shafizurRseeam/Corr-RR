[![arXiv](https://img.shields.io/badge/arXiv-2505.15483-<COLOR>.svg)](https://arxiv.org/abs/2505.15483)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[PETS'26] Frequency Estimation of Correlated Multi-attribute Data under Local Differential Privacy
 

**Contributions:** 

*This paper proposes a two-phase LDP Framework, Correlated Randomized Response (Corr-RR), for Multi-attribute Correlated Data.
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

Tested environments: `uv` version `0.7.11` and Python version `3.12`~`3.13`.

**Install UV package manager.**
This project is packaged by `uv`, a modern Python package management system similar to `miniconda` or `poetry`.
All dependencies are listed in `pyproject.toml`.
We recommend using `uv` to create a virtual environment and install the dependencies.


To install `uv`, follow the instructions in the "[uv installation](https://docs.astral.sh/uv/)".

Here is a quick guide to install it in windows using powershell. 

After installation, follow the prompts to add `uv` to your system's `PATH`.
You can verify the installation by running the following command in your terminal (Windows, Linux, or macOS):


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

## Runtime Comparison (Windows Xeon W-2145 vs. MacBook Pro M2 Pro)
*(Approximate runtimes; values rounded for readability.)*

| Figure Group                                              | Windows (Xeon W-2145, 32 GB RAM) | macOS (M2 Pro, 16 GB RAM) |
|-----------------------------------------------------------|-----------------------------------|----------------------------|
| **Fig 2**                                                 | ~2 sec                               | ~1 sec                        |
| **Fig 3 (a,b,c), Fig 4 (a,b,c)**                          | ~75 min                            | ~28 min                     |
| **Fig 5 (a,b,c), Fig 6 (a,b,c), Fig 13 (a,b,c), Fig 14**  | ~80 min                            | ~30 min                     |
| **Fig 7 (a,b,c), Fig 8 (a,b,c)**                          | —                                 | ~75 min                     |
| **Fig 9 (a,b,c), Fig 10 (a,b,c)**                         | ~45 min                            | ~15 min                     |
| **Fig 11 (a,b,c)**                                        | ~18min / ~14min / ~23min                   | —                          |
| **Fig 12 (a,b,c)**                                        | ~3 sec                               | ~1 sec                        |
| **Table 2**                                               | ~1 sec                               | ~2 sec                        |
| **Table 3**                                               | ~1 sec                               | ~1 sec                        |
| **Tables 4 & 7**                                          | ~3 min                             | ~25 sec                       |
| **Tables 5 & 8**                                          | ~13 min                            | ~4 min                      |
| **Tables 6 & 9**                                          | ~75 min                             | ~30 min                     |



## Placeholder Sections (You can fill later)

### 📘 Introduction
(Add a short overview of the Corr-RR mechanism and goals.)

### ⚙️ Installation
(Explain how to install dependencies or set up environment.)

### ▶️ Running Experiments
(Show commands like: `python reproduction/fig_2.py`)

### 📁 Project Structure
(Brief explanation of folders: reproduction/, src/, data/, etc.)

