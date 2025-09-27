import pandas as pd

data = {
    'DefectID': ['D1','D2','D3','D4','D5'],
    'Module': ['Login','Payment','Reports','Login','Payment'],
    'Severity': ['High','Medium','Low','High','Medium'],
    'Status': ['Open','Closed','Open','Closed','Open']
}

df = pd.DataFrame(data)

print("Open Defects:")
print(df[df['Status']=="Open"])

print("High Severity Defects:")
print(df[df['Severity']=="High"])

print("Defect Count by Status:")
print(df.groupby("Status")["DefectID"].count())
