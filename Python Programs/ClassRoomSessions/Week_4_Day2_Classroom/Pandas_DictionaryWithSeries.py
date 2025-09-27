import pandas as pd
TestDataFrame = {
    'Alex': pd.Series([10,20,30], index=['Jan', 'Feb', 'Mar']),
    'Man': pd.Series([20,30,40], index=['Jan', 'Feb', 'Mar'])
}
df = pd.DataFrame(TestDataFrame)
print(df)