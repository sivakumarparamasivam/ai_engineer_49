import pandas as pd
import numpy as np


df = pd.read_csv('test_results.csv')
df.columns = df.columns.str.strip() 


print("\n=== Original Data ===")
print(df)


print("\n=== Missing Values Count ===")
missing_values = df.isna().sum()
print(missing_values)


df_cleaned = df.copy()


df_cleaned['Duration'] = pd.to_numeric(df_cleaned['Duration'], errors='coerce')
mean_duration = df_cleaned['Duration'].mean()
df_cleaned['Duration'] = df_cleaned['Duration'].fillna(mean_duration)


df_cleaned['Status'] = df_cleaned['Status'].fillna('Unknown')


df_cleaned['Defects'] = pd.to_numeric(df_cleaned['Defects'], errors='coerce')
mean_defects = df_cleaned['Defects'].mean()
df_cleaned['Defects'] = df_cleaned['Defects'].fillna(mean_defects)

# Display data after filling missing values
print("\n=== Data after filling missing values ===")
print(df_cleaned)

# Drop any remaining rows with missing values
df_final = df_cleaned.dropna()

print("\n=== Final Data after dropping any remaining missing values ===")
print(df_final)

# Save the cleaned dataset
df_final.to_csv('test_results_cleaned.csv', index=False)
print("\nCleaned data saved to 'test_results_cleaned.csv'")

# Print summary statistics of numeric columns
print("\n=== Summary Statistics of Numeric Columns ===")
print(df_final.describe())