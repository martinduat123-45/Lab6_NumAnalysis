import pandas as pd
import numpy as np
import os

print("Available files:", os.listdir())

file_name = None
for file in os.listdir():
    if file.endswith(".csv") and "Programming" in file:
        file_name = file
        break

if file_name is None:
    raise FileNotFoundError("CSV file not found")

df = pd.read_csv(file_name)
df.columns = df.columns.str.strip()

print("\nPreview:")
print(df.head())

df["Month"] = pd.to_datetime(df["Month"], errors="coerce")

languages = ['C#', 'Flutter', 'Java', 'JavaScript', 'Matlab', 'PhP', 'Python', 'React', 'Swift', 'TypeScript']
languages = sorted(languages)

student_id = 250204
index = student_id % 1000 % 10

assigned_language = languages[index]
print("Assigned Language:", assigned_language)

col = None
for c in df.columns:
    if assigned_language.lower() in c.lower():
        col = c
        break

if col is None:
    raise KeyError("Assigned language column not found")

df_lang = df[["Month", col]].copy()
df_lang.columns = ["Month", "Popularity"]

df_lang["Growth_Rate"] = df_lang["Popularity"].pct_change() * 100
df_lang["Moving_Avg"] = df_lang["Popularity"].rolling(6).mean()
df_lang["Moving_STD"] = df_lang["Popularity"].rolling(6).std()

mean_growth = df_lang["Growth_Rate"].mean()
std_growth = df_lang["Growth_Rate"].std()

conditions = [
    df_lang["Growth_Rate"] > mean_growth,
    (df_lang["Growth_Rate"] > 0) & (df_lang["Growth_Rate"] <= mean_growth),
    df_lang["Growth_Rate"].abs() <= 1,
    df_lang["Growth_Rate"] < -std_growth
]

choices = ["Growth", "Introduction", "Maturity", "Decline"]

df_lang["Lifecycle_Phase"] = np.select(conditions, choices, default="Stable")

print(df_lang.head())
print("\nPhase Distribution:")
print(df_lang["Lifecycle_Phase"].value_counts())

lang1 = languages[index]
lang2 = languages[(index + 1) % 10]

print("Language 1:", lang1)
print("Language 2:", lang2)

col1 = None
col2 = None

for c in df.columns:
    if lang1.lower() in c.lower():
        col1 = c
    if lang2.lower() in c.lower():
        col2 = c

if col1 is None or col2 is None:
    raise KeyError("Language columns not found")

df_pair = df[["Month", col1, col2]].copy()
df_pair.columns = ["Month", "Lang_A", "Lang_B"]

mean_a = df_pair["Lang_A"].mean()
mean_b = df_pair["Lang_B"].mean()

std_a = df_pair["Lang_A"].std()
std_b = df_pair["Lang_B"].std()

corr = np.corrcoef(df_pair["Lang_A"].fillna(0), df_pair["Lang_B"].fillna(0))[0, 1]

dominance_ratio = (df_pair["Lang_A"] > df_pair["Lang_B"]).sum() / len(df_pair) * 100

cross_over = df_pair[df_pair["Lang_A"] > df_pair["Lang_B"]]

norm_a = (df_pair["Lang_A"] - mean_a) / std_a
norm_b = (df_pair["Lang_B"] - mean_b) / std_b

rpi = (norm_a - norm_b).mean()

summary = pd.DataFrame({
    "Mean_A": [mean_a],
    "Mean_B": [mean_b],
    "Std_A": [std_a],
    "Std_B": [std_b],
    "Correlation": [corr],
    "Dominance_Ratio_%": [dominance_ratio],
    "RPI": [rpi]
})

print("\nSummary:")
print(summary)

print("\nCrossover months:", len(cross_over))