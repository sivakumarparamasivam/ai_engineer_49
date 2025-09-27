import numpy as np
import pandas as pd

a1 = np.array([10,20,30])
a2 = np.array([30,40,50])
df = pd.DataFrame([a1,a2],columns=['A','B','C'])
print(df)
