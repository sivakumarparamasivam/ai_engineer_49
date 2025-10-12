from sklearn.preprocessing import StandardScaler
import numpy as np
data= np.array([[1, 2], [3, 4], [5, 6]])

scaler = StandardScaler()

# print("Fit Method", scaler.fit(data))

# print("Transform Method", scaler.transform(data))

scaled_data= scaler.fit_transform(data)

print("Original Data")
print("*"*100)
print(data)
print("Scaled Data")
print("*"*100)
print(scaled_data)