import pandas as pd

# Create a simple array (list of numbers)
data = [10, 20, 30, 40, 50]

# Convert to pandas Series (1D array)
series = pd.Series(data)
print(series)

# Convert to pandas DataFrame (2D array / table)
df = pd.DataFrame(data, columns=["Numbers"])
print(df)
