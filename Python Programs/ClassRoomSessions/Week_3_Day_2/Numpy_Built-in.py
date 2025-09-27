import numpy as np

#1.Creating
execution_times = np.array([10, 15, 20, 25, 30, 35, 40, 45])
print("Original 1D array:", execution_times)

#2.Indexing & Shaping
print("\nIndexing:")
print("First element:", execution_times[0])
print("Last element:", execution_times[-1])
print("Third element:", execution_times[2])

print("Shape of the array:", execution_times.shape)

#3.Slicing
print("\nSlicing:")
print("Execution times of the first 3 tests:", execution_times[0:3])
print("Every alternate test time:", execution_times[::2])

#4.Iteration
print("\nIteration:")
for i, t in enumerate(execution_times,1):
    print(f"Test {i} execution time: {t} seconds")

#5.Reshaping
reshaped_array = execution_times.reshape((2, 4))
print("\nReshaped Array (2x4):")
print(reshaped_array)

#6.Joining
array_1 = np.array([50, 55, 60, 65])
combined_array = np.concatenate([execution_times, array_1])
print("\nCombined Array after Joining:")
print(combined_array)

#7.Splitting
split_arrays = np.array_split(combined_array,3)
print("\nSplit Arrays:")
for i, arr in enumerate(split_arrays, start=1):
    print(f"Part {i}:", arr)

execution_times = np.array([10, 15, 20, 25, 30, 35, 40, 45])
print("Original 1D array:", execution_times)