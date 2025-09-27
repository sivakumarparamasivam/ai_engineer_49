import pandas as pd
import numpy as np

# Creates a Pandas Series representing test execution times:
execution_times = pd.Series([12, 15, 20, 18, 25, 30, 22],index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
print("Execution Times Series:")
print(execution_times)

# slice mid of the elements
print("\nSliced Execution Times (indices 2 to 4):")
print(execution_times['c':'e'])


# Create with numpy array of number of defects [10,20,23,45,50] convert to series
defects_array = np.array([10, 20, 23, 45, 50])
defects_series = pd.Series(defects_array)
print("\nDefects Series from NumPy Array:")
print(defects_series)
print(defects_series[::-1])  # Accessing value by index


# Create series with the help of dictionary for the foll test cases executed by Engineers as key
engineer_tests = {"Alex": 500, "Steve": 200, "Bob": 300}
engineer_series = pd.Series(engineer_tests)
print("\nEngineer Test Cases Series:")
print(engineer_series)
print(engineer_series['Steve'])  # Accessing value by key
print(engineer_series.iloc[1])
print(engineer_series.loc['Bob'])  # Accessing value by position