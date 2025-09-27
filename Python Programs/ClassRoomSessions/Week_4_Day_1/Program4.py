import pandas as pd
pass_rates = pd.Series(
    [80, 85, 78, 90, 88],
    index=['B1', 'B2', 'B3', 'B4', 'B5']
)
#Print the Series
print("=== Test Pass Percentage Across Builds ===")
print(pass_rates)

#Calculate and print average pass rate
avg_pass_rate = pass_rates.mean()
print("\n=== Average Pass Rate ===")
print(avg_pass_rate)

#Find which build had the highest pass rate
print("\n=== Build with Highest Pass Rate ===")
print(pass_rates.idxmax(), ":", pass_rates.max())

#iloc → pass rate of the last build
print("\n=== Pass Rate of Last Build (using iloc) ===")
print(pass_rates.iloc[-1])

#loc → pass rate of Build B3
print("\n=== Pass Rate of Build B3 (using loc) ===")
print(pass_rates.loc['B3'])


#Normalize values (subtract average from each pass rate)
normalized = pass_rates - avg_pass_rate
print("\n=== Normalized Pass Rates (deviation from average) ===")
print(normalized)
