import pandas as pd
s1 = pd.Series([10,20,30], index=['a','b','c'])
s2 = pd.Series([40,50,60], index=['a','b','c'])
df = pd.DataFrame([s1,s2])
print(df)
