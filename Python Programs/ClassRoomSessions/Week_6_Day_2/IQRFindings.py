import pandas as pd

csv_path = '/Users/sivakumarparamasivam/Sivakumar/python_workspace/ai_engineer_2025/Python Programs/ClassRoomSessions/Week_6_Day_2/SalesDataset.csv'
df = pd.read_csv(csv_path)
Q1 = df['Total Amount'].quantile(0.25)
Q3 = df['Total Amount'].quantile(0.75)

# Find out IQR Value
IQR_Value= Q3 - Q1

print("IQR Value", IQR_Value)

# Find out Lower and Upper Bound
lBound = Q1 - 1.5 * IQR_Value
uBound = Q3 + 1.5 * IQR_Value

# Find out the outliers

outliers = df[(df['Total Amount']< lBound) | (df['Total Amount'] > uBound)]
print("*" * 100)
print(outliers)
print("*" * 100)
outlier_data= outliers[["Date","Gender","Age","Product Category","Quantity","Price per Unit","Total Amount"]]

outlier_data.to_csv('/Users/sivakumarparamasivam/Sivakumar/python_workspace/ai_engineer_2025/Python Programs/ClassRoomSessions/Week_6_Day_2/outliers.csv',index=True)

outliers = df[(df['Total Amount']> lBound) & (df['Total Amount']< uBound)]

# outlier_cleaned_Data = df.drop[outliers]

outlier_cleaned_Data= outliers[["Date","Gender","Age","Product Category","Quantity","Price per Unit","Total Amount"]]

outlier_cleaned_Data.to_csv('/Users/sivakumarparamasivam/Sivakumar/python_workspace/ai_engineer_2025/Python Programs/ClassRoomSessions/Week_6_Day_2/outliers_cleaned_data.csv',index=True)



