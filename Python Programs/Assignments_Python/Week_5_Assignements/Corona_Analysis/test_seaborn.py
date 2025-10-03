import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Create some sample data
np.random.seed(0)
data = np.random.randn(100)

# Try to create a simple seaborn plot
plt.figure(figsize=(8, 6))
sns.histplot(data=data, kde=True)
plt.title('Test Seaborn Plot')
plt.savefig('test_seaborn_plot.png')
plt.close()

print("If you see this message and no errors above, seaborn is working correctly!")