import pandas as pd
import numpy as np
import os


csv_path = '/Users/sivakumarparamasivam/Sivakumar/python_workspace/ai_engineer_2025/Python Programs/ClassRoomSessions/Week_6_Day_1/SalesDataset.csv'
df = pd.read_csv(csv_path)

# Percentile
print('************************************Percentile*********************************')

print("\n=== 25th Percentile for Total Amount Column ===")
per25 = df['Total Amount'].quantile(0.25)
print(per25)
print("\n=== 50th Percentile for Total Amount Column ===")
per50 = df['Total Amount'].quantile(0.50)
print(per50)
print("\n=== 75th Percentile for Total Amount Column ===")
per75 = df['Total Amount'].quantile(0.75)
print(per75)

# Variance
print('************************************Variance*********************************')
TotalAmountVariance = df['Total Amount'].var()
print("\n=== Total Amount Column Variance ===")
print(TotalAmountVariance)

QuantityVariance = df['Quantity'].var()
print("\n=== Quantity Column Variance ===")
print(QuantityVariance)

#Correlations
print('************************************Coorelations*********************************')
print("\n=== Age and Total Amount Corr ===")
ageTotalAmountcorr = df["Age"].corr(df["Total Amount"])
print(ageTotalAmountcorr)
print("\n=== Quanity and Total Amount Corr ===")
qtyTotalAmountcorr = df["Quantity"].corr(df["Total Amount"])
print(qtyTotalAmountcorr)
print("\n=== Price per Unit and Total Amount Corr ===")
priceTotalAmountcorr = df["Price per Unit"].corr(df["Total Amount"])
print(priceTotalAmountcorr)

print(df[['Age','Price per Unit', 'Total Amount']].corr())



