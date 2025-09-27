import pandas as pd

data = {
    'TestCase': ['TC1','TC2','TC3','TC4','TC5', 'TC6'],
    'Status': ['Passed','Failed','Passed','Failed','Passed','Failed'],
    'Duration': [12,15,20,18,25,None]
}

df = pd.DataFrame(data)

# print(df)

print(df['Status'])

print(df[df['Status']=="Failed"])

df.to_csv('test_results.csv', index=False)

new_df = pd.read_csv('test_results.csv')

print("##################Duration Mean Value###########3")

print(new_df['Duration'].mean())

print("##################################################")

new_df['Duration'] = new_df['Duration'].fillna(new_df['Duration'].mean())

print(new_df)
