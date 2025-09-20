import numpy as np
# ---------------------------
# a) Generate synthetic data
# ---------------------------
np.random.seed(42)  # For reproducibility
data = np.random.randint(5, 51, size=(5, 50))  # 5 cycles × 50 tests
print("Dataset Shape:", data.shape)
print("Sample (first row):", data[0])

# ---------------------------
# b1) Statistical Analysis
# ---------------------------
print("\n--- Statistical Analysis ---")
avg_per_cycle = np.mean(data, axis=1)
print("Average execution time per cycle:", avg_per_cycle)

max_value = np.max(data)
max_position = np.unravel_index(np.argmax(data), data.shape)
print("Maximum execution time in dataset:", max_value, "at (cycle, test):", max_position)

std_per_cycle = np.std(data, axis=1)
print("Standard deviation per cycle:", std_per_cycle)

# ---------------------------
# b2) Slicing Operations
# ---------------------------
print("\n--- Slicing Operations ---")
print("First 10 tests from Cycle 1:", data[0, :10])
print("Last 5 tests from Cycle 5:", data[4, -5:])
print("Every alternate test from Cycle 3:", data[2, ::2])

# ---------------------------
# b3) Arithmetic Operations
# ---------------------------
print("\n--- Arithmetic Operations ---")
add_cycles = data[0] + data[1]
sub_cycles = data[0] - data[1]
print("Element-wise addition (Cycle 1 + Cycle 2):", add_cycles[:10], "...")  # preview first 10
print("Element-wise subtraction (Cycle 1 - Cycle 2):", sub_cycles[:10], "...")

mul_cycles = data[3] * data[4]
div_cycles = data[3] / data[4]
print("Element-wise multiplication (Cycle 4 * Cycle 5):", mul_cycles[:10], "...")
print("Element-wise division (Cycle 4 / Cycle 5):", div_cycles[:10], "...")

# ---------------------------
# b4) Power Functions
# ---------------------------
print("\n--- Power Functions ---")
squared = np.power(data, 2)
cubed = np.power(data, 3)
sqrt_vals = np.sqrt(data)
log_vals = np.log(data + 1)
print("Squared sample (first 5 of Cycle 1):", squared[0, :5])
print("Cubed sample (first 5 of Cycle 1):", cubed[0, :5])
print("Square root sample (first 5 of Cycle 1):", sqrt_vals[0, :5])
print("Log-transformed sample (first 5 of Cycle 1):", log_vals[0, :5])

# ---------------------------
# b5) Copy Operations
# ---------------------------
print("\n--- Copy Operations ---")
shallow_copy = data.view()
shallow_copy[0, 0] = 999  # modify shallow copy
print("After shallow copy modification, original[0,0]:", data[0, 0])

deep_copy = data.copy()
deep_copy[0, 1] = 888  # modify deep copy
print("After deep copy modification, original[0,1]:", data[0, 1])

# ---------------------------
# b6) Filtering with Conditions
# ---------------------------
print("\n--- Filtering with Conditions ---")
cycle2_above30 = data[1, data[1] > 30]
print("Cycle 2 tests > 30s:", cycle2_above30)

consistent_above25 = np.all(data > 25, axis=0)
print("Tests consistently > 25s across all cycles:", np.where(consistent_above25)[0])

thresholded_data = data.copy()
thresholded_data[thresholded_data < 10] = 10
print("First row after thresholding (<10 → 10):", thresholded_data[0, :10])
