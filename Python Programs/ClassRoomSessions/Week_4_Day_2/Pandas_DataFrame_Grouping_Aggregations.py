import pandas as pd

data = {
    'TestCase': ['TC1','TC2','TC3','TC4','TC5','TC6'],
    'Module': ['Login','Login','Payment','Payment','Reports','Reports'],
    'Status': ['Passed','Failed','Passed','Failed','Passed','Passed'],
    'Duration': [12,15,20,18,25,22]
}

df = pd.DataFrame(data,columns=['TestCase','Module','Status','Duration'])

print(df)

status_count = df.groupby("Status")["TestCase"].count()
module_avg = df.groupby("Module")["Duration"].mean()

print("Count by Status:")
print(status_count)
print("Average Duration by Module:")
print(module_avg)

print("Passed:", df[df.Status=="Passed"]["TestCase"].to_list())
print("Failed:", df[df.Status=="Failed"]["TestCase"].to_list())
