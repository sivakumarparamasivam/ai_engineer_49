import pandas as pd
import numpy as np

# --- Base Class ---
class DataLoader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.df = None

    def load(self):
        """Load CSV file into DataFrame"""
        self.df = pd.read_csv(self.filepath)
        return self.df


# --- Derived Class for Analysis ---
class CovidAnalyzer(DataLoader):
    def __init__(self, filepath):
        super().__init__(filepath)
        self.df = self.load()

    def summarize_by_region(self):
        return self.df.groupby("WHO Region")[["Confirmed", "Deaths", "Recovered"]].sum()

    def filter_low_cases(self, threshold=10):
        return self.df[self.df["Confirmed"] >= threshold]

    def region_with_highest_confirmed(self):
        summary = self.summarize_by_region()
        return summary.loc[summary["Confirmed"].idxmax()]

    def sort_by_confirmed(self, out_file="sorted_cases.csv"):
        sorted_df = self.df.sort_values(by="Confirmed", ascending=False)
        sorted_df.to_csv(out_file, index=False)
        return sorted_df

    def top_countries(self, n=5):
        return self.df.nlargest(n, "Confirmed")[["Country/Region", "Confirmed", "Deaths", "Recovered"]]

    def region_with_lowest_deaths(self):
        summary = self.summarize_by_region()
        return summary.loc[summary["Deaths"].idxmin()]

    def india_summary(self):
        return self.df[self.df["Country/Region"] == "India"][["Country/Region", "Confirmed", "Deaths", "Recovered"]]

    def mortality_rate_by_region(self):
        summary = self.summarize_by_region()
        summary["Mortality Rate (%)"] = (summary["Deaths"] / summary["Confirmed"]) * 100
        return summary[["Confirmed", "Deaths", "Mortality Rate (%)"]]

    def recovery_rate_by_region(self):
        summary = self.summarize_by_region()
        summary["Recovery Rate (%)"] = (summary["Recovered"] / summary["Confirmed"]) * 100
        return summary[["Confirmed", "Recovered", "Recovery Rate (%)"]]

    def detect_outliers(self):
        mean = self.df["Confirmed"].mean()
        std = self.df["Confirmed"].std()
        lower, upper = mean - 2 * std, mean + 2 * std
        outliers = self.df[(self.df["Confirmed"] < lower) | (self.df["Confirmed"] > upper)]
        return outliers, lower, upper

    def group_by_country_region(self):
        return self.df.groupby(["WHO Region", "Country/Region"])[["Confirmed", "Deaths", "Recovered"]].sum()

    def zero_recovered(self):
        return self.df[self.df["Recovered"] == 0][["Country/Region", "WHO Region", "Confirmed", "Deaths", "Recovered"]]


# --- Example Usage ---
if __name__ == "__main__":
    filepath = "Python Programs/Assignments_Python/Week_4_Assignments/country_wise_latest.csv"   # Update path if needed
    analyzer = CovidAnalyzer(filepath)

    print("1. Case Summary by Region:\n", analyzer.summarize_by_region(), "\n")
    print("2. Filtered (Confirmed >= 10):\n", analyzer.filter_low_cases().head(), "\n")
    print("3. Region with Highest Confirmed:\n", analyzer.region_with_highest_confirmed(), "\n")
    print("4. Sorted Data (saved to CSV):\n", analyzer.sort_by_confirmed().head(), "\n")
    print("5. Top 5 Countries by Cases:\n", analyzer.top_countries(), "\n")
    print("6. Region with Lowest Deaths:\n", analyzer.region_with_lowest_deaths(), "\n")
    print("7. India’s Case Summary:\n", analyzer.india_summary(), "\n")
    print("8. Mortality Rate by Region:\n", analyzer.mortality_rate_by_region(), "\n")
    print("9. Recovery Rate by Region:\n", analyzer.recovery_rate_by_region(), "\n")
    outliers, lower, upper = analyzer.detect_outliers()
    print(f"10. Outliers (Confirmed outside {lower:.2f} - {upper:.2f}):\n", outliers, "\n")
    print("11. Group by Country and Region:\n", analyzer.group_by_country_region().head(), "\n")
    print("12. Countries with Zero Recovered:\n", analyzer.zero_recovered(), "\n")
