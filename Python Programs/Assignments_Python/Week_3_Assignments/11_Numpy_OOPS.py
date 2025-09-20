import numpy as np

# Base class
class TestReport:
    def __init__(self, execution_times: np.ndarray):
        self.execution_times = execution_times

    def average_time(self):
        return np.mean(self.execution_times)

    def max_time(self):
        return np.max(self.execution_times)


# Subclass
class RegressionReport(TestReport):
    def __init__(self, execution_times: np.ndarray):
        super().__init__(execution_times)

    def slow_tests(self, threshold: float):
        return self.execution_times[self.execution_times > threshold]


# Main section
if __name__ == "__main__":
    # Create NumPy array with 10 execution times
    times = np.array([12.4, 9.8, 15.6, 8.3, 22.5, 18.7, 5.2, 14.1, 7.9, 20.0])

    # Create RegressionReport object
    report = RegressionReport(times)

    # Display results
    print("Average Execution Time:", report.average_time())
    print("Maximum Execution Time:", report.max_time())
    print("Slow Tests (> 15s):", report.slow_tests(15))