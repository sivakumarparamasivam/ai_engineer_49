import pandas as pd

defects = pd.Series(
    [5, 8, 3, 6, 10, 2, 7],
    index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
)


print(defects)

print(" Maximum Defects Logged in a Day")
print(defects.max())


print("Day with Minimum Defects")
print(defects.idxmin())  


print(" Defects on Day5 (using iloc)")
print(defects.iloc[4])

print(" Defects on Wednesday (using loc)")
print(defects.loc['Wed'])

print("Total Defects in the Week")
print(defects.sum())
