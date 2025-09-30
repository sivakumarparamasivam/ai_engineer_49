import matplotlib.pyplot as plt

test_status = ['Passed', 'Failed', 'Skipped']
test_counts = [45, 10, 5]
colors = ['green', 'red', 'orange']

plt.bar(test_status, test_counts, color=colors, edgecolor="green", width=0.75, align='center', label="Defect Status",
        fontsize='10')


plt.title('Test Execution Results')
plt.xlabel('Test Status')
plt.ylabel('Number of Test Cases')
plt.show()
