from sklearn.preprocessing import MinMaxScaler, RobustScaler
import numpy as np
data= np.array([[1, 2], [3, 4], [5, 6],[7,8],[9,10]])

# MinMax Scaler
print('*'*100)
print('MinMaxScaler')
print('*'*100)

minMaxScaler = MinMaxScaler()

minmax_scaled_data= minMaxScaler.fit_transform(data)

print(minmax_scaled_data)

#Robust Scaler
print('*'*100)
print('Robust Scaler')
print('*'*100)

robustScaler = RobustScaler()
#test
robustScaler.fit(data)
print(robustScaler.center_)
print(np.percentile(data,25, axis=0))
print(np.percentile(data,75, axis=0))

robust_scaled_data= robustScaler.fit_transform(data)

print(robust_scaled_data)
