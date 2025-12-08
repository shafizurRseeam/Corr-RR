import os
import pandas as pd
import numpy as np
from itertools import combinations


# -------------------------------------------------------------
# Detect project root (same logic you use everywhere)
# -------------------------------------------------------------
if "__file__" in globals():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
else:
    project_root = os.path.abspath(os.path.join(os.getcwd(), ".."))


# -------------------------------------------------------------
# Compute dataset statistics
# -------------------------------------------------------------
def dataset_stats(df):
    cols = df.columns.tolist()
    d = len(cols)

    # domain size = maximum number of categories among attributes
    domain_size = max(len(df[c].unique()) for c in cols)

    num_users = len(df)

    # Pearson correlation (absolute)
    corr_mat = df.corr(numeric_only=True)
    corr_vals = []
    for c1, c2 in combinations(df.columns, 2):
        corr_vals.append(abs(corr_mat.loc[c1, c2]))

    if corr_vals:
        corr_min = round(min(corr_vals), 3)
        corr_max = round(max(corr_vals), 3)
        corr_range = (corr_min, corr_max)
    else:
        corr_range = ("N/A", "N/A")

    return d, domain_size, num_users, corr_range


# -------------------------------------------------------------
# MAIN — prints statistics for all .csv in a given folder
# -------------------------------------------------------------
if __name__ == "__main__":

    # YOU ONLY NEED TO CHANGE THIS
    dataset_folder = "preprocessed_data"

    folder_path = os.path.join(project_root, dataset_folder)

    print("\n=== REAL-WORLD DATASET STATISTICS ===\n")
    #print("Project root:", project_root)
    #print("Dataset folder:", folder_path)
    print()

    # Load all CSV files in folder
    for filename in os.listdir(folder_path):

        if not filename.endswith(".csv"):
            continue

        dataset_name = filename.replace(".csv", "")
        full_path = os.path.join(folder_path, filename)

        print(f"Dataset: {dataset_name}")
        #print(f"  Path: {full_path}")

        df = pd.read_csv(full_path)

        # Encode categorical columns
        df_enc = df.copy()
        for col in df_enc.columns:
            df_enc[col] = df_enc[col].astype("category").cat.codes

        d, dom, users, corr = dataset_stats(df_enc)

        print(f"  d (num attributes):      {d}")
        print(f"  |D| (max domain size):   {dom}")
        print(f"  # Users:                 {users}")
        print(f"  Correlation range:       {corr[0]} to {corr[1]}")
        print("----------------------------------------")

