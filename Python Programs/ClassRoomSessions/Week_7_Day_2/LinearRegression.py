from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('/Users/sivakumarparamasivam/Sivakumar/python_workspace/ai_engineer_2025/Python Programs/ClassRoomSessions/Week_7_Day_2/salary_1.csv')

X= data[['YearsExperience']]
y= data['Salary']

# print(X)
# print(y)

X_train, X_test , y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

print (X_test)
y_pred = model.predict(X_test)
print(y_pred)

# df = pd.DataFrame({
#     'YOE': y_test,         # Actual values
#     'Predicted': y_pred    # Predicted values
# }) 
# df.to_csv('./predicted.csv')


# print("MSE", mean_squared_error(y_test, y_pred))
# print("R Square Score" , r2_score(y_test, y_pred))

# plt.scatter(X_test, y_test, color='green', label='Actual')
# plt.plot(X_test, y_pred, color='blue', label='Predicted')
# plt.xlabel('Years of Experience')
# plt.ylabel('Salary')
# plt.title('Salary Prediction')
# plt.legend()
# plt.show()
