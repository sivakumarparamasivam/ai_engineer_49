import pandas as pd
import matplotlib.pyplot as plt

data = {'Module': ['AI', 'ML', 'Python', 'DataStructures'],
        'Teamsize': [135, 125, 125, 115]}

df = pd.DataFrame(data)

plt.pie(df['Teamsize'], labels=df['Module'], autopct='%1.1f%%', startangle=90)
plt.title('Team Size Distribution by Module')
plt.axis('equal')
plt.show()
