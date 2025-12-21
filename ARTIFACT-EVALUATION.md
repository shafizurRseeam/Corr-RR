# Artifact Appendix

Paper title: Frequency Estimation of Correlated Multi-attribute Data under Local Differential Privacy (PETS'26)

Authors : Shafizur Rahman Seeam, Ye Zheng, and Yidan Hu. 

To cite the paper, please use the following BibTeX:

@article{seeam2025frequency,
  title={Frequency Estimation of Correlated Multi-attribute Data under Local Differential Privacy},
  author={Seeam, Shafizur Rahman and Zheng, Ye and Hu, Yidan},
  journal={arXiv preprint arXiv:2507.17516},
  year={2025}
}

Artifacts HotCRP Id: #20

Requested Badge: Available, Functional, Reproduced

## Description
This paper studies frequency estimation of multi-attribute correlated data under LDP. Our artifact includes the source code and preprocessed datasets necessary to reproduce the experimental results presented in the paper.

We have simplified the reproduction process and have created separate scripts for individual figures and subfigures. Some figures could be generated within a few seconds while others could take several minutes depending on the hardware. The scripts are expected to produce the same results for all the figures and tables (with minor variation due to the randomness). Detailed runtime is provided so as to give reviewers the idea of the expected time each script would take to run. 

### Security/Privacy Issues and Ethical Concerns (All badges)
The artifact does not require any security modifications for installation or execution. The dataset used is publicly  available, and we used a smaller subset of those datasets, with no sensitive information involved.
 
## Basic Requirements (Only for Functional and Reproduced badges)
### Hardware Requirements
Standard hardware with a typical CPU and 16GB of memory should be sufficient. We tested the artifact on:
* Intel® Xeon® W-2145 CPU (8 cores / 16 threads, 3.70 GHz) and 32 GB RAM
* 14-inch MacBook Pro with an Apple M2 processor 10 cores and 16 GB RAM.


### Software Requirements
The artifact is expected to run on newer versions of Windows, Ubuntu, and macOS, but only the versions listed below were explicitly tested. Development was carried out using:
* Python (Version 3.13.7)
* VS Code (Version 1.107.1) 
* Jupyter Notebook (Version 7.3.2)

The artifact was tested on the following operating systems:

* Microsoft Windows 11 Enterprise (OS Version 10.0.26100, Build 26100) 
* Ubuntu (Version 24.04.3 LTS)
* macOS Ventura (version 13.4.1).

All Python dependencies are fully specified in `pyproject.toml` and are installed automatically using the `uv` package manager. No additional system-level packages are required.

### Estimated Time and Storage Consumption
Reproducing all figures and tables is computationally intensive due to extensive simulations. Expected runtimes vary by hardware:
* Installing dependencies with uv sync typically takes 3–5 minutes.
* Approximate Runtimes for Figures

| Paper Figure (Per Subplot)                   | Windows (Xeon W-2145, 32GB RAM) | Apple M2 (10-core CPU, 16 GB RAM) |
|---------------------------------------------|----------------------------------|----------------------------|
| **Fig. 2**                                   | ~2 sec                           | ~1 sec                    |
| **Fig. 3 (a,b,c), Fig. 4 (a,b,c)**           | ~75 min each                         | ~28 min each                  |
| **Fig. 5 (a,b,c), Fig. 6 (a,b,c)**           | ~80 min  each                        | ~30 min  each                 |
| **Fig. 7 (a,b,c), Fig. 8 (a,b,c)**           | ~220 min each                         | ~75 min each                  |
| **Fig. 9 (a,b,c), Fig. 10 (a,b,c)**          | ~45 min each                         | ~15 min  each                 |
| **Fig. 11 (a,b,c)**                           | (~18, ~14, ~23) min each                 | (~8, ~5, ~10) min  each              |
| **Fig. 12 (a,b,c)**                           | ~3 sec each                          | ~1 sec  each                  |
| **Fig. 13 (a,b,c), Fig. 14 (a,b,c)**         | ~80 min  each                        | ~30 min  each                 |

* Approximate Runtimes for Tables

| Table Numbers          | Windows (Xeon W-2145, 32GB RAM) | Apple M2 (10-core CPU, 16 GB RAM) |
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
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
**macOS / Linux**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

After installation, you may need to restart the terminal for `uv` to be available in PATH. Then verify installation with:

```
uv --version
```


You should be in the project root directory, which contains the `pyproject.toml` file. 
Then, run the following `uv` command:

```
uv sync
```

This command creates a virtual environment in `.venv` in the project root and installs the dependencies listed in `pyproject.toml`.

### Testing the Environment (Only for Functional and Reproduced badges)
Tested with: 
* `uv` version `0.9.17` on macOS and `0.9.18` on Windows Desktop
* Python versions `3.11`–`3.13`

To verify that the dependencies have been installed correctly, run the following command from the project root:
```
uv pip check
```

This checks dependency compatibility and reports any conflicts. The exact number of packages and runtime may vary across platforms. A successful check should report that all installed packages are compatible. Expected output, where N and T would vary: 

```
Checked N packages in T ms
All installed packages are compatible
```

## Artifact Evaluation (Only for Functional and Reproduced badges)

### Main Results and Claims
#### Main Result 1: Impact of Privacy Budget
(Figure 3–4, Page 9) Corr-RR demonstrates smaller MSE compared to baselines (SPL, RS+FD, RS+RFD) across all privacy budget ($\epsilon=0.1$ to $\epsilon=0.5$).

#### Main Result 2: Impact of Number of Attributes.

(Figure 5-6, Page 9-10) and (Figure 13-14, Page 17) Corr-RR demonstrates lower rise in MSE compared to baselines (SPL, RS+FD, RS+RFD) as attributes ($d=2$ to $d=6$) size increases.

#### Main Result 3: Impact of Correlations. 

(Figure 7-8, Pages 10) In Corr-RR, MSE decreases as correlation becomes stronger ($\rho=0.1$ to $\rho=0.9$), while the baselines (SPL, RS+FD, RS+RFD) show a relatively flat line, indicating that correlation has little to no effect on the baselines.  

#### Main Result 4: Impact of the Size of Phase I Users.
(Figure 9–10, Page 12) Baselines SPL and RS+FD are single phase only thus show no change. Baseline RS+RFD and our proposed solution Corr-RR are two-phase and shows significant change. The overall MSE increase if Phase I size is higher. Typically 10-20% users in Phase I provides a good overall split. We provide more fine-grained results in Table 4-9 in Page 18-19

#### Main Result 5: Results on Real-world Data. 

(Figure 11, Page 12) Corr-RR demonstrates lower MSE than baselines (SPL, RS+FD, RS+RFD). However, we see for the Mushroom dataset, Corr-RR is not the best due the nature of the dataset (highly skewed), as explained in the paper and this is supported by Figure 12 (Page 17).

#### Other Results:
(Figure 2, Page 6) shows the results for correlation-aware probability $p_y$ as we change the marginals, (Table 2, Page 8) shows the correlation of synthetic datasets as we change the correlation, and (Table 3, Page 8) shows the characteristics of real-world datasets. 



You can reproduce these results using the provided scripts. Two options are available:

1. Use the main reproduction scripts in the `reproduction` folder. (Option 1)
2. Run individual notebook in the `experiments_notebook` folder. (Option 2)

### Experiments -- Option 1 (Quick) -- Recommended

Expected runtimes and storage requirements for each figure and table are summarized in the "Estimated Time and Storage Consumption" section above. The `reproduction` folder contains scripts for reproducing all figures and tables.

```
|- reproduction
  |- all_experiments.py
  |- fig_2.py: Figure 2 (<1 Sec)
  |- fig_3a.py: Figure 3a  (<28 minute)
  |- table_2.py: Table 2  (<1 sec)
  |- ...

```

You can run these scripts directly with `uv run` (no need to manually activate the environment) to generate Figures and Tables. Run any script from the project root. To reproduce all the results at once, simply use

```
uv run ./reproduction/all_experiments.py
```
* This command creates a folder named `generated_results` in the project root and saves all generated figures in PDF format and tables in TXT and CSV formats. Each script produces an output file with a matching name (e.g., `fig_3a.py` generates `fig_3a.pdf`, `table_2.py` generates `table_2.txt`, and `table_3.py` generates `table_3.csv`). Since this script runs all experiments sequentially, it may take a substantial amount of time. For faster validation, we recommend running individual scripts corresponding to specific figures or tables.


To generate individual experiments, simply run the following from root. (Recommended)

```
uv run ./reproduction/fig_3a.py
```
* To reproduce any result, simply replace `fig_3a.py` with the desired script from the `reproduction` folder (e.g., `fig_2.py`, `fig_3a.py`,`table_2.py`, etc.).
Results should match those in the paper (minor randomness expected).


#### Experiment 1: Impact of Privacy Budget (Figure 3–4, Page 9).

To reproduce the first result, from the project root run: 

```
uv run ./reproduction/fig_3a.py
```
* To reproduce the other subplots, simply replace `fig_3a.py` with the desired script from the `reproduction` folder (e.g., `fig_3b.py`, `fig_3c.py`,`fig_4a.py`,`fig_4b.py`,`fig_4c.py`).

#### Experiment 2: Impact of Number of Attributes (Figure 5-6, Page 9-10, and Figure 13-14, Page 17).

```
uv run ./reproduction/fig_5a.py
```
* To reproduce the other subplots for, simply replace `fig_5a.py` with the desired script from the `reproduction` folder (e.g., `fig_5b.py`, `fig_5c.py`,`fig_6a.py`,`fig_6b.py`,`fig_6c.py`, `fig_13a.py`,`fig_13b.py`, `fig_13c.py`,`fig_14a.py`,`fig_14b.py`,`fig_14c.py`).


#### Experiment 3: Impact of Correlations (Figure 7-8, Pages 10).

```
uv run ./reproduction/fig_7a.py
```
* To reproduce the other subplots, simply replace `fig_7a.py` with the desired script from the `reproduction` folder (e.g., `fig_7b.py`, `fig_7c.py`,`fig_8a.py`,`fig_8b.py`,`fig_8c.py`).

#### Experiment 4: Impact of the Size of Phase I Users (Figure 9–10, Page 11, and Table 4-9, Page 18-19).

```
uv run ./reproduction/fig_9a.py
```
* To reproduce the other subplots, simply replace `fig_9a.py` with the desired script from the `reproduction` folder (e.g., `fig_9b.py`, `fig_9c.py`,`fig_10a.py`,`fig_10b.py`,`fig_10c.py`, `table_4.py`,`table_5.py`, `table_6.py`,`table_7.py`,`table_8.py`,`table_9.py`).

#### Experiment 5: Results on Real-world Data (Figure 11, Page 12). 
```
uv run ./reproduction/fig_11a.py
```
* To reproduce the other subplots, simply replace `fig_11a.py` with the desired script from the `reproduction` folder (e.g., `fig_11b.py`,`fig_11c.py`,).


#### Other Figures and Tables (Figure 2, Figure 12, Table 2, and Table 3)
```
uv run ./reproduction/fig_2.py
```
* To reproduce the other subplots, simply replace `fig_2.py` with the desired script from the `reproduction` folder (e.g., `table_2`,`table_3`, `fig_12a.py`, `fig_12b.py`,`fig_12c.py`).



Following is the summarized scripts mapping to individual results in the paper:

| Claim | Figures / Tables | Script(s) |
|------|------------------|-----------|
| Impact of Privacy Budget | Figure 3–4 | fig_3a.py, fig_3b.py, fig_3c.py, fig_4a.py, fig_4b.py, fig_4c.py |
| Impact of Attributes | Figure 5–6, 13–14 | fig_5a.py, fig_5b.py, fig_5c.py, fig_6a.py, fig_6b.py, fig_6c.py,  fig_13a.py, fig_13b.py, fig_13c.py, fig_14a.py, fig_14b.py, fig_14c.py |
| Impact of Correlation | Figure 7–8 | fig_7a.py, fig_7b.py, fig_7c.py, fig_8a.py, fig_8b.py, fig_8c.py |
| Phase I Size | Figure 9–10, Table 4–9 | fig_9a.py, fig_9b.py, fig_9c.py, fig_10a.py, fig_10b.py, fig_10c.py, table_4.py, table_5.py, table_6.py, table_7.py, table_8.py, table_9.py |
| Real-world Data | Figure 11–12 | fig_11a.py, fig_11b.py, fig_11c.py, fig_12a.py, fig_12b.py, fig_12c.py |
| Others | Figure 2, Table 2–3 | fig_2.py, table_2.py, table_3.py |

### Experiments -- Option 2 (Detailed)


The `experiments_notebook` folder contains self-contained Jupyter notebooks for interactive exploration: 

```
|- experiments_notebook
  |- misc.ipynb
  |- MSE_vs_Attribute.ipynb
  |- MSE_vs_Budget.ipynb
  |- MSE_vs_Correlation.ipynb
  |- Phase_Tables.ipynb
  |- real_dataset_histogram.ipynb
  |- real_world_experiment.ipynb
```
Users can modify parameters to explore different experimental settings.

## Limitations (Only for Functional and Reproduced badges)
All the figures should be produced exactly as it is with only minor differences due to the randomness that is not noticeable. We did not omit any figures and tables used in the experiments and provided scripts to generate every table and figures used. 
