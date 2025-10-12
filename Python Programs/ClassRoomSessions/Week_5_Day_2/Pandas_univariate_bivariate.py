import pandas as pd

df = pd.read_csv("test_results.csv")

print("#################################")
print("\nUnivariate Analysis: Duration")

print("Duration Distribution:")
print(df["Duration"])

mean_duration = df["Duration"].mean()
median_duration = df["Duration"].median()
std_duration = df["Duration"].std()

print(f"Mean Duration: {mean_duration}")
print(f"Median Duration: {median_duration}")
print(f"Standard Deviation of Duration: {std_duration}")

print("#################################")

print("\nFull Description:")
print(df["Duration"].describe())

print("#################################")
print("\nBivariate Analysis: Status vs Duration (Average Duration by Status):")
status_duration_avg = df.groupby("Status")["Duration"].mean()
print(status_duration_avg)
print("#################################")

print("\nMultivariate Analysis: Module vs Status vs Defects (Total Defects):")
module_status_defects = df.groupby(["Module", "Status"])["Defects"].sum()
print(module_status_defects)
print("#################################")

# customer.service@hdfc.com


