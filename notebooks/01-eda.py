# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.5
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # 01 — Exploratory Data Analysis: Wine Quality (Red)
#
# Quick EDA on the UCI Wine Quality dataset.
# Dataset is DVC-tracked; run `dvc pull` first.

# %%
import sys
from pathlib import Path

for _p in [Path.cwd(), Path.cwd().parent]:
    if (_p / "src").is_dir():
        sys.path.insert(0, str(_p))
        break

import matplotlib.pyplot as plt

from src.data import drop_duplicates, load_raw

# %% [markdown]
# ## Load raw data

# %%
df = load_raw()
print(f"Shape: {df.shape}")
df.head()

# %% [markdown]
# ## Schema and null counts

# %%
df.info()
df.isna().sum()

# %% [markdown]
# ## Duplicate rows

# %%
print(f"Duplicates: {df.duplicated().sum()}")
df_clean = drop_duplicates(df)
print(f"After drop: {df_clean.shape}")

# %% [markdown]
# ## Target distribution — quality

# %%
df_clean["quality"].value_counts().sort_index().plot(kind="bar")
plt.title("Wine Quality distribution")
plt.xlabel("quality")
plt.ylabel("count")
plt.tight_layout()
plt.show()

# %% [markdown]
# ## Feature correlations with quality

# %%
corr = df_clean.corr(numeric_only=True)["quality"].sort_values(ascending=False)
corr
