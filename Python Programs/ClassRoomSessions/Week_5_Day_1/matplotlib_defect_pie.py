import matplotlib.pyplot as plt

values = [10, 15, 5]
labels = ["High", "Medium", "Low"]

plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=45)
plt.title("Defect Distribution by Severity")
plt.show()
