import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('data1.csv')

df.set_index('Day', inplace=True)

fig, axes = plt.subplots(3, 1)

# Line plot
df.plot(kind='line', ax=axes[0], title='Line Plot')

# Bar plot
df.plot(kind='bar', ax=axes[1], title='Bar Plot')

# Histogram — Flatten all week values into a single series
df.plot(kind='hist', bins=10, ax=axes[2], title='Histogram')

# Final layout
plt.tight_layout()
plt.show()
