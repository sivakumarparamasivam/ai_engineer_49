import pandas as pd
import numpy as np

# Read the CSV file
df = pd.read_csv('/Users/sivakumarparamasivam/Sivakumar/python_workspace/ai_engineer_2025/Python Programs/ClassRoomSessions/Week_6_Day_1/test_results.csv')

# Display original data
print("\n=== Original Data ===")
print(df)

# Count missing values in each column
print("\n=== Missing Values Count ===")
missing_values = df.isnull().sum()
print(missing_values)

# Convert Duration to numeric, handling any non-numeric values
df['Duration'] = pd.to_numeric(df['Duration'], errors='coerce')

# Calculate mean duration
mean_duration = df['Duration'].mean()

# Fill missing values
# - Duration: replace with mean
# - Status: replace with "Unknown"
df['Duration'] = df['Duration'].fillna(mean_duration)
df['Status'] = df['Status'].fillna("Unknown")
s

print("\n=== Data after filling Duration and Status ===")
print(df)

# Drop any remaining rows with missing values
df_cleaned = df.dropna()

print("\n=== Final Cleaned Data ===")
print(df_cleaned)

# Save the cleaned data
df_cleaned.to_csv('test_results_cleaned.csv', index=False)
print("\nCleaned data has been saved to 'test_results_cleaned.csv'")

