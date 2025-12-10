# Artifact Appendix

Paper title: Frequency Estimation of Correlated Multi-attribute Data under Local Differential Privacy


Requested Badge: Available, Functional, Reproduced

## Description
This paper studies Frequency estimation of multi-attribute corrlated data under LDP. Our artifact includes the source code and preprocessed datasets necessary to reproduce the experimental results presented in the paper.

We have simplified the reproduction process and have created seperated scripts for individual figures presented in the paper. Some figures could be generated within few seconds while others could take several minutes depending on the hardware. The scripts are expected to produce the same results for all the figures and tables (with minor variation due to the randomness). Detailed runtime is provided so as to give reviewers the idead of the expected time each script would take to run. 

### Security/Privacy Issues and Ethical Concerns (All badges)
The artifact does not require any security modifications for installation or execution. The dataset used is publickly avalavle, and we used a smaller subset of those datasets, with no sensitive information involved.

## Basic Requirements (Only for Functional and Reproduced badges)
### Hardware Requirements
The code has been tested on Linux/Windows desktops and macOS laptops. Standard hardware with a typical CPU and 16GB of memory should be sufficient. We used Xeon W-2145, 32GB RAM desktop and Macbook Pro (M2, 16GB RAM) for all the experiments.  

### Software Requirements
The artifact is implemented entirely in Python. It only requires a working Python environment. Development was done using Jupyter Notebook and VS Code, and the artifact has been tested on various Windows, Linux and macOS systems.

### Estimated Time and Storage Consumption
Reproducing all figures and tables in this artifact is computationally intensive due to the large number of simulations. The runtimes vary significantly depending on the machine, but users should expect:

* Installing dependencies with uv sync typically takes 1–2 minutes.
* Running all figure and table scripts sequentially (across all subplots) may require several hours, depending on hardware. Each subplot runs independently, and users may selectively execute individual scripts as needed.



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

* **Storage**: The complete environment (including dependencies and preprocessed datasets) requires approximately 350 MB.

## Environment 
### Accessibility (All badges)

GitHub repository: https://github.com/ZhengYeah/Optimal-GPM/

Commits after `4c8b33f` (dated June 4) are expected to work.

### Set up the environment (Only for Functional and Reproduced badges)

**Install UV package manager.** This project is packaged by `uv`, a modern Python package management system similar to `miniconda` or `poetry`.

All dependencies are listed in `pyproject.toml`.

We recommend using `uv` to create a virtual environment and install the dependencies. To install `uv`, follow the instructions in the "[uv installation](https://docs.astral.sh/uv/)".

After installation, follow the prompts to add `uv` to your system's `PATH`. You can verify the installation by running the following command in your terminal (Windows, Linux, or macOS):

```
uv --version
```
This should display the installed version of `uv`.

**Install dependencies.** Download the artifact from the GitHub repository and navigate to the project root directory:

```
git clone https://github.com/ZhengYeah/Optimal-GPM.git
cd Optimal-GPM
```

You should be in the project root directory, which contains the `pyproject.toml` file. 
Then, run the following `uv` command:

```
[PROJECT_ROOT]$ uv sync
```

This command creates a virtual environment in the project root and installs the dependencies listed in `pyproject.toml`. 

### Testing the Environment (Only for Functional and Reproduced badges)
To verify that the dependencies have been installed correctly, run the following command from the project root:
```
[PROJECT_ROOT]$ uv pip check
```

This will print: all installed packages are compatible.

## Artifact Evaluation (Only for Functional and Reproduced badges)

### Main Results and Claims
#### Main Result 1: Comparison with PM-C and SW-C
(Figure 8–11, Page 10) OGPM demonstrates smaller expected errors compared to PM-C and SW-C.

#### Main Result 2: Comparison with Original PM and SW

(Figure 12, Page 11) OGPM shows smaller expected errors than the original PM and SW mechanisms on their respective data domains.

#### Main Result 3: Comparison with Other Mechanisms

(Figure 13–15, Pages 11–12) OGPM is compared with other non-piecewise-based mechanisms, showing improved performance in expected error.

#### Main Result 4: Comparison of Estimations on Real-world Datasets

(Figure 16–17, Page 12) OGPM is tested on real-world datasets, outperforming PM-C and SW-C in terms of accuracy.

You can reproduce these results using the provided scripts. Two options are available:

1. Use the main reproduction scripts in the `reproduction` folder. (Option 1)
2. Run individual scripts in the `experiments` folder. (Option 2)

### Experiments -- Option 1 (Quick) -- Recommended

The `reproduction` folder contains scripts  to reproduce key results from the paper. The structure is as follows:

```
|- reproduction
  |- figure_8_11.py: Figure 8a, 9a, 10a, 11b (Page 10)  (<1 minute)
  |- figure_12.py: Figure 12a and 12b (Page 11)  (<1 minute)
  |- figure_13_15.py: Figure 13a, 14, 15 (Page 11~12)  (<1 minute)
  |- figure_16_17.py: Figure 16a and 17a (Page 12)  (subsampled, <5 minutes)
```

You can run these scripts directly with `uv run` (no need to manually activate the environment). For example, to generate the first group of figures:

```
[PROJECT_ROOT]$ uv run ./reproduction/figure_8_11.py
```

This will display the corresponding figures using matplotlib.

Some figures are omitted due to minor parameter differences, for brevity. The last script is a subsampled version of the original one to speed up the reproduction. It may slightly differ from the original figure in the paper, but the overall trend remains the same. The fine-grained results can be obtained by running the scripts in the `experiments` folder.

#### Experiment 1: Comparison with PM-C and SW-C

To reproduce the first result, run 

```
[PROJECT_ROOT]$ uv run ./reproduction/figure_8_11.py
```

#### Experiment 2: Comparison with Original PM and SW

```
[PROJECT_ROOT]$ uv run ./reproduction/figure_12.py
```

#### Experiment 3: Comparison with Other Mechanisms

```
[PROJECT_ROOT]$ uv run ./reproduction/figure_13_15.py
```

#### Experiment 4: Comparison of Estimations on Real-world Datasets

```
[PROJECT_ROOT]$ uv run ./reproduction/figure_16_17.py
```

### Experiments -- Option 2 (Detailed)

The `experiments` folder contains all scripts used in the paper, including intermediate results and full figures. These scripts rely on PyCharm’s path configuration. To run them, you need the PyCharm GUI and run them by right-clicking the script.

If you have installed `uv`, you can select it as the interpreter in PyCharm. PyCharm will then automatically create a virtual environment and install all dependencies specified in `pyproject.toml`.
For detailed instructions, see the official guide: [PyCharm: configure a uv environment](https://www.jetbrains.com/help/pycharm/uv.html).

After setting up the environment, there should be no package import errors. Then you can run the scripts by opening them and right-clicking in the PyCharm editor and selecting "Run `file_name.py`".

The scripts are organized as follows:

```
|- experiments
  |- theoretical
    |- classical_domain
      |- whole_domain_L1.py: Figure 8
      |- worst_case_L1.py, worst-case_L2.py: Figure 9
      |- comparison_truncated_and_staircase: Figure 13 and 14
      |- small_epsilon: Figure 20 in the appendix
    |- circular_domain
      |- whole_domain_circular_L2.py: Figure 10
      |- worst_case_circular_L1.py, worst-case_circular_L2.py: Figure 11
      |- comparison_purkayastha: Figure 15
    |- ablation
      |- ablation_whole_domain_L2_PM.py: Figure 12(a)
      |- ablation_whole_domain_L2_SW.py: Figure 12(b)
  |- experimental
    |- distribution_classical.py, distribution_circular.py: Figure 16
    |- mean_classical.py, mean_circular.py: Figure 17
```

The above scripts will generate `.csv` files containing the results, which are also included in corresponding folders.
Then the PDF plots can be generated by running the scripts beginning with `draw_*` in the same folder.

## Limitations (Only for Functional and Reproduced badges)
In the quick reproduction, some figures are omitted due to minor parameter differences, for brevity. The fine-grained results can be found in the option 2.
