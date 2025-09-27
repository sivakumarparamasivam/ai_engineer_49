import pandas as pd

execution_times = pd.Series(
        [12, 15, 20, 18, 25, 30, 22],
        index=['TC1', 'TC2', 'TC3', 'TC4', 'TC5', 'TC6', 'TC7']
    )

# Print the Series
print("=== Test Execution Times Series ===")
print(execution_times)

#Display the first 3 test times
print("\n=== First 3 Test Times ===")
print(execution_times.head(3))

#Find the mean execution time
print("\n=== Mean Execution Time ===")
print(execution_times.mean())

#Use iloc to print the 2nd test time (index-based)
print("\n=== 2nd Test Time using iloc ===")
print(execution_times.iloc[1])

#Use loc to print execution time of TC3 (label-based)
print("\n=== Execution Time of TC3 using loc ===")
print(execution_times.loc['TC3'])

