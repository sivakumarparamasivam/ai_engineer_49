import matplotlib.pyplot as plt

weeks = [1, 2, 3, 4, 5, 6, 7, 8, 9]
defects = [5, 8, 6, 10, 7, 4, 19, 25, 12]

plt.plot(weeks, defects, marker='P', color='green', linestyle='--', linewidth=2.5)
plt.title("Defect Trend Over Time")
plt.xlabel("Week Number")
plt.ylabel("Number of Defects")
plt.grid(True)
plt.savefig('test.jpg')
plt.show()

