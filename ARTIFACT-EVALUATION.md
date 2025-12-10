# Artifact Appendix

Paper title: Frequency Estimation of Correlated Multi-attribute Data under Local Differential Privacy


Requested Badge: Available, Functional, Reproduced

## Description
This paper studies frequency estimation of multi-attribute correlated data under LDP. Our artifact includes the source code and preprocessed datasets necessary to reproduce the experimental results presented in the paper.

We have simplified the reproduction process and have created seperate scripts for individual figures. Some figures could be generated within few seconds while others could take several minutes depending on the hardware. The scripts are expected to produce the same results for all the figures and tables (with minor variation due to the randomness). Detailed runtime is provided so as to give reviewers the idea of the expected time each script would take to run. 

### Security/Privacy Issues and Ethical Concerns (All badges)
The artifact does not require any security modifications for installation or execution. The dataset used is publicly  available, and we used a smaller subset of those datasets, with no sensitive information involved.

## Basic Requirements (Only for Functional and Reproduced badges)
### Hardware Requirements
The code has been tested on Linux/Windows desktops and macOS laptops. Standard hardware with a typical CPU and 16GB of memory should be sufficient. We used Xeon W-2145, 32GB RAM desktop and Macbook Pro (M2, 16GB RAM) for all the experiments.  

### Software Requirements
The artifact is implemented entirely in Python. It only requires a working Python environment. Development was done using Jupyter Notebook and VS Code, and the artifact has been tested on various Windows, Linux and macOS systems.

### Estimated Time and Storage Consumption
Reproducing all figures and tables in this artifact is computationally intensive due to the large number of simulations. The runtimes vary significantly depending on the machine, but users should expect:


Approximate Runtimes for Figures

| Paper Figure (Per Subplot)                   | Windows (Xeon W-2145, 32GB RAM) | macOS (M2 Pro, 16GB RAM) |
|---------------------------------------------|----------------------------------|----------------------------|
| **Fig. 2**                                   | ~2 sec                           | ~1 sec                    |
| **Fig. 3 (a,b,c), Fig. 4 (a,b,c)**           | ~75 min each                         | ~28 min each                  |
| **Fig. 5 (a,b,c), Fig. 6 (a,b,c)**           | ~80 min  each                        | ~30 min  each                 |
| **Fig. 7 (a,b,c), Fig. 8 (a,b,c)**           | ~220 min each                         | ~75 min each                  |
| **Fig. 9 (a,b,c), Fig. 10 (a,b,c)**          | ~45 min each                         | ~15 min  each                 |
| **Fig. 11 (a,b,c)**                           | (~18, ~14, ~23) min                 | (~8, ~5, ~10) min                |
| **Fig. 12 (a,b,c)**                           | ~3 sec each                          | ~1 sec  each                  |
| **Fig. 13 (a,b,c), Fig. 14 (a,b,c)**         | ~80 min  each                        | ~30 min  each                 |

Approximate Runtimes for Tables

| Table Numbers          | Windows (Xeon W-2145, 32GB RAM) | macOS (M2 Pro, 16GB RAM) |
|------------------------|----------------------------------|----------------------------|
| **Table 2**            | ~1 sec                           | ~2 sec                    |
| **Table 3**            | ~1 sec                           | ~1 sec                    |
| **Tables 4 & 7**       | ~3 min  each                         | ~25 sec  each                 |
| **Tables 5 & 8**       | ~13 min  each                        | ~4 min  each                  |
| **Tables 6 & 9**       | ~75 min   each                       | ~30 min   each                |

* **Storage**: The complete environment (including dependencies and preprocessed datasets) requires approximately 520 MB.

## Environment 
### Accessibility (All badges)

GitHub repository: https://github.com/shafizurRseeam/Corr-RR.git


Commits after `XXXX` (dated December X) are expected to work.

### Set up the environment (Only for Functional and Reproduced badges)


**Cloning the repository.** Download the artifact from the GitHub repository and navigate to the project root directory:

```bash
git clone https://github.com/shafizurRseeam/Corr-RR.git
cd Corr-RR
```

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


You should be in the project root directory, which contains the `pyproject.toml` file. 
Then, run the following `uv` command:

```
[PROJECT_ROOT]$ uv sync
```

This command creates a virtual environment in the project root and installs the dependencies listed in `pyproject.toml`. 

### Testing the Environment (Only for Functional and Reproduced badges)
Tested environments: `uv` version `0.9.16` and Python versions `3.11`–`3.13`.
To verify that the dependencies have been installed correctly, run the following command from the project root:
```
[PROJECT_ROOT]$ uv pip check
```

This will print: all installed packages are compatible.

## Artifact Evaluation (Only for Functional and Reproduced badges)

### Main Results and Claims
#### Main Result 1: Impact of Privacy Budget
(Figure 3–4, Page 9) Corr-RR demonstrates smaller MSE compared to baselines (SPL, RS+FD, RS+RFD) across all privacy budget ($\epsilon=0.1$ to $\epsilon=0.5$).

#### Main Result 2: Impact of Number of Attributes.

(Figure 5-6, Page 9-10) and (Figure 13-14, Page 17) Corr-RR demonstrates loswer rise in MSE compared to baselines (SPL, RS+FD, RS+RFD) as attributes ($d=2$ to $d=6$) size increases.

#### Main Result 3: Impact of Correlations. 

(Figure 7-8, Pages 10) In Corr-RR, MSE decreases as correlation becomes stronger ($\rho=0.1$ to $\rho=0.9$), while the baselines (SPL, RS+FD, RS+RFD) show a relatively flat line, indicating that correlation has little to no effect on the baselines.  

#### Main Result 4: Impact of the Size of Phase I Users.
(Figure 9–10, Page 12) Baselines SPL and RS+FD are single phase only thus shows no change. Baseline RS+RFD and our proposed solution Corr-RR are two-phase and shows significant change. The overall MSE increase if Phase I size is higher. Typically 10-20% users in Phase I provides an overall good split. We provide more fine-grained results in from Table 4-9 in Page 18-19

#### Main Result 5: Results on Real-world Data. 

(Figure 11, Page 12) Corr-RR demostrates lower MSE than baselines (SPL, RS+FD, RS+RFD). However, we see for the Mushroom dataset, Corr-RR is not the best due the the nature of the dataset (highly skewed), as explained in the paper and this is supprted by Figure 12 (Page 17).


You can reproduce these results using the provided scripts. Two options are available:

1. Use the main reproduction scripts in the `reproduction` folder. (Option 1)
2. Run individual notebook in the `experiments_notebook` folder. (Option 2)

### Experiments -- Option 1 (Quick) -- Recommended

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
* To reproduce any result, simply replace `fig_3a.py` with the desired script from the `reproduction` folder (e.g., `fig_2.py`, `fig_3a.py`,`table_2.py`, etc.).
Results should match those in the paper (minor randomness expected).

#### Experiment 1: Impact of Privacy Budget (Figure 3–4, Page 9).

To reproduce the first result, run 

```
[PROJECT_ROOT]$ uv run ./reproduction/fig_3a.py
```
* To reproduce the other subplots, simply replace `fig_3a.py` with the desired script from the `reproduction` folder (e.g., `fig_3a.py`,`fig_3b.py`, `fig_3c.py`,`fig_4a.py`,`fig_4b.py`,`fig_4c.py`).

#### Experiment 2: Impact of Number of Attributes (Figure 5-6, Page 9-10, and Figure 13-14, Page 17).

```
[PROJECT_ROOT]$ uv run ./reproduction/fig_5a.py
```
* To reproduce the other subplots for, simply replace `fig_5a.py` with the desired script from the `reproduction` folder (e.g., `fig_5a.py`,`fig_5b.py`, `fig_5c.py`,`fig_6a.py`,`fig_6b.py`,`fig_6c.py`, `fig_13a.py`,`fig_13b.py`, `fig_13c.py`,`fig_14a.py`,`fig_14b.py`,`fig_14c.py`).


#### Experiment 3: Impact of Correlations (Figure 7-8, Pages 10).

```
[PROJECT_ROOT]$ uv run ./reproduction/fig_7a.py
```
* To reproduce the other subplots, simply replace `fig_7a.py` with the desired script from the `reproduction` folder (e.g., `fig_7a.py`,`fig_7b.py`, `fig_7c.py`,`fig_8a.py`,`fig_8b.py`,`fig_8c.py`).

#### Experiment 4: Impact of the Size of Phase I Users (Figure 9–10, Page 12, and Table 4-9, Page 18-19).

```
[PROJECT_ROOT]$ uv run ./reproduction/fig_9a.py
```
* To reproduce the other subplots, simply replace `fig_9a.py` with the desired script from the `reproduction` folder (e.g., `fig_9a.py`,`fig_9b.py`, `fig_9c.py`,`fig_10a.py`,`fig_10b.py`,`fig_10c.py`, `table_4.py`,`table_5.py`, `table_6.py`,`table_7.py`,`table_8.py`,`table_9.py`).

#### Experiment 5: Results on Real-world Data (Figure 11, Page 12). 
```
[PROJECT_ROOT]$ uv run ./reproduction/fig_11a.py
```
* To reproduce the other subplots, simply replace `fig_11a.py` with the desired script from the `reproduction` folder (e.g., `fig_11b.py`,`fig_11c.py`,).


#### Other Figures and Tables (Figure 2, Figure 12, Table 2, and Table 3)
```
[PROJECT_ROOT]$ uv run ./reproduction/fig_2.py
```
* To reproduce the other subplots, simply replace `fig_2.py` with the desired script from the `reproduction` folder (e.g., `table_2`,`table_3`, `fig_12a.py`, `fig_12b.py`,`fig_12c.py`,).

### Experiments -- Option 2 (Detailed)


The `experiments_notebook` folder contains self-contained Jupyter notebooks for interactive exploration: 

```
|- experiments_notebook
  |- misc.ipynb
  |- MSE_vs_Attribute.ipynb
  |- MSE_vs_Budget.ipynb
  |- ........

```
Users can modify parameters to explore different experimental settings.

## Limitations (Only for Functional and Reproduced badges)
All the figures should be produced exactly as it is and any changes, due to the randomness of the experiments, will not be noticed. We did not ommit any figures and tables used in the experiments and provided scripts to generate every table and figures used. 
