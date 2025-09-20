import numpy as np

# Class definitions
class ManualTester:
    def analyze(self, data: np.ndarray):
        print("ManualTester → First 5 test execution times:", data[:5])


class AutomationTester:
    def analyze(self, data: np.ndarray):
        print("AutomationTester → Fastest test case:", np.min(data))


class PerformanceTester:
    def analyze(self, data: np.ndarray):
        print("PerformanceTester → 95th percentile execution time:", np.percentile(data, 95))


# Function to demonstrate polymorphism
def show_analysis(tester, data: np.ndarray):
    tester.analyze(data)


# Main section
if __name__ == "__main__":
    # Create NumPy array with at least 12 execution times
    times = np.array([12.4, 9.8, 15.6, 8.3, 22.5, 18.7, 5.2, 
                      14.1, 7.9, 20.0, 11.3, 16.4])

    # Create tester objects
    manual = ManualTester()
    automation = AutomationTester()
    performance = PerformanceTester()

    # Call show_analysis for each tester
    show_analysis(manual, times)
    show_analysis(automation, times)
    show_analysis(performance, times)
