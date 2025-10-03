import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Setup visualization directory
VIZ_DIR = "/Users/sivakumarparamasivam/Sivakumar/python_workspace/ai_engineer_2025/Python Programs/Assignments_Python/Week_5_Assignements/Corona_Analysis/visualization"
os.makedirs(VIZ_DIR, exist_ok=True)

# 1. Load Data
df = pd.read_csv("/Users/sivakumarparamasivam/Sivakumar/python_workspace/ai_engineer_2025/Python Programs/Assignments_Python/Week_5_Assignements/Corona_Analysis/country_wise_latest.csv")

# 2. Clean Data
df.replace("inf", np.nan, inplace=True)
numeric_cols = [
    "Confirmed", "Deaths", "Recovered", "Active", "New cases", "New deaths", "New recovered",
    "Deaths / 100 Cases", "Recovered / 100 Cases", "Deaths / 100 Recovered",
    "Confirmed last week", "1 week change", "1 week % increase"
]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")
df["Country/Region"] = df["Country/Region"].str.replace(r"[*]", "", regex=True)

# 3. Analysis
print("Summary statistics:")
print(df.describe())
print("\nMissing values per column:")
print(df.isnull().sum())

# 4. Basic Visualizations
plt.figure(figsize=(10,6))
df.groupby("WHO Region")["Confirmed"].sum().plot(kind="bar")
plt.title("Confirmed Cases by WHO Region")
plt.ylabel("Confirmed Cases")
plt.tight_layout()
plt.savefig(os.path.join(VIZ_DIR, "confirmed_by_region.png"))
plt.close()

plt.figure(figsize=(10,6))
df.nlargest(10, "Confirmed").plot(x="Country/Region", y="Confirmed", kind="bar")
plt.title("Top 10 Countries by Confirmed Cases")
plt.ylabel("Confirmed Cases")
plt.tight_layout()
plt.savefig(os.path.join(VIZ_DIR, "top10_countries_confirmed.png"))
plt.close()

# 5. Advanced Analysis and Visualizations
plt.figure(figsize=(12,8))
correlation = df[numeric_cols].corr()
plt.imshow(correlation, cmap="coolwarm", aspect="auto")
plt.colorbar()
plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=90)
plt.yticks(range(len(correlation.columns)), correlation.columns)
plt.title("Correlation Heatmap of COVID-19 Metrics")
plt.tight_layout()
plt.savefig(os.path.join(VIZ_DIR, "correlation_heatmap.png"))
plt.close()

# WHO Region Analysis
region_stats = df.groupby("WHO Region").agg({
    "Confirmed": ["sum", "mean", "count"],
    "Deaths": ["sum", "mean"],
    "Recovered": ["sum", "mean"],
    "Active": ["sum", "mean"]
}).round(2)
print("\nRegion-wise Statistics:")
print(region_stats)

# Pie Chart of Deaths by Region
plt.figure(figsize=(10,8))
death_by_region = df.groupby("WHO Region")["Deaths"].sum()
plt.pie(death_by_region, labels=death_by_region.index, autopct="%1.1f%%")
plt.title("Distribution of Deaths by WHO Region")
plt.savefig(os.path.join(VIZ_DIR, "deaths_by_region_pie.png"))
plt.close()

# Recovery Rate Analysis
plt.figure(figsize=(12,6))
df["Recovery Rate"] = (df["Recovered"] / df["Confirmed"] * 100).round(2)
df.nlargest(10, "Recovery Rate").plot(x="Country/Region", y="Recovery Rate", kind="bar")
plt.title("Top 10 Countries by Recovery Rate")
plt.ylabel("Recovery Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(VIZ_DIR, "top10_recovery_rate.png"))
plt.close()

# Death Rate Analysis
plt.figure(figsize=(12,6))
df["Death Rate"] = (df["Deaths"] / df["Confirmed"] * 100).round(2)
df.nlargest(10, "Death Rate").plot(x="Country/Region", y="Death Rate", kind="bar")
plt.title("Top 10 Countries by Death Rate")
plt.ylabel("Death Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(VIZ_DIR, "top10_death_rate.png"))
plt.close()

# Save enriched dataset
df.to_csv(os.path.join(VIZ_DIR, "covid_analysis_results.csv"), index=False)

print("\nAnalysis Results:")
print(f"Total Countries Analyzed: {len(df)}")
print(f"Total Confirmed Cases: {df['Confirmed'].sum():,}")
print(f"Total Deaths: {df['Deaths'].sum():,}")
print(f"Total Recovered: {df['Recovered'].sum():,}")
print(f"Average Recovery Rate: {df['Recovery Rate'].mean():.2f}%")
print(f"Average Death Rate: {df['Death Rate'].mean():.2f}%")

# Region with highest cases
highest_cases_region = df.groupby("WHO Region")["Confirmed"].sum().idxmax()
print(f"\nRegion with highest cases: {highest_cases_region}")

# Countries with zero deaths
zero_death_countries = df[df["Deaths"] == 0]["Country/Region"].tolist()
print(f"\nCountries with zero deaths: {', '.join(zero_death_countries)}")

# Countries with 100% recovery rate
full_recovery = df[df["Recovery Rate"] >= 99.9]["Country/Region"].tolist()
print(f"\nCountries with ≥99.9% recovery rate: {', '.join(full_recovery)}")

print(f"\nVisualization files have been saved in: {VIZ_DIR}")