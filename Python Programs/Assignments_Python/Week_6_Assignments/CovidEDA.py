import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

class CovidEDA:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
        self.df_selected = None
        self.df_cleaned = None
        self.df_scaled = None

    def load_and_select_data(self):
        self.data = pd.read_csv(self.file_path)
        cols_to_keep = ['Confirmed', 'New cases']
        self.df_selected = self.data[cols_to_keep].copy()
        
        print("--- 1. Data Loading and Selection ---")
        print("Selected Data Head:")
        print(self.df_selected.head())
        print("\nSelected Data Info:")
        self.df_selected.info()
        print("-" * 40)
        return self.df_selected

    def compute_stats(self):
        if self.df_selected is None:
            print("Error: Data not loaded. Call load_and_select_data first.")
            return

        print("--- 2. Statistical Measures (Original Data) ---")
        
        print("Mean:\n", self.df_selected.mean(numeric_only=True))
        print("\nMedian:\n", self.df_selected.median(numeric_only=True))
        print("\nVariance:\n", self.df_selected.var(numeric_only=True))
        print("\nStandard Deviation:\n", self.df_selected.std(numeric_only=True))
        
        corr_matrix = self.df_selected.corr()
        print("\nCorrelation Matrix:\n", corr_matrix)
        print("-" * 40)
        return corr_matrix

    def remove_outliers_iqr(self):
        if self.df_selected is None:
            print("Error: Data not loaded. Call load_and_select_data first.")
            return

        print("--- 3. Outlier Detection and Removal (IQR) ---")
        
        df = self.df_selected.copy()
        
        def iqr_outlier_remover(series):
            Q1 = series.quantile(0.25)
            Q3 = series.quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            return (series >= lower_bound) & (series <= upper_bound)

        outlier_mask_confirmed = iqr_outlier_remover(df['Confirmed'])
        outlier_mask_newcases = iqr_outlier_remover(df['New cases'])

        combined_mask = outlier_mask_confirmed & outlier_mask_newcases
        
        self.df_cleaned = df[combined_mask] 

        # testing

        print(f"Original shape: {df.shape}")
        print(f"Cleaned shape (after removing {df.shape[0] - self.df_cleaned.shape[0]} rows): {self.df_cleaned.shape}")

        print("\nCleaned Dataset Head:")
        print(self.df_cleaned.head())
        print("\nCleaned Dataset Descriptive Stats:")
        print(self.df_cleaned.describe())
        
        self.df_cleaned.to_csv('cleaned_covid_data.csv', index=False)
        
        print("-" * 40)
        return self.df_cleaned

    def normalize_data(self):
        if self.df_cleaned is None:
            print("Error: Data not cleaned. Call remove_outliers_iqr first.")
            return

        print("--- 4. Normalization using Standard Scaler ---")
        
        scaler = StandardScaler()

        scaled_data = scaler.fit_transform(self.df_cleaned)

        self.df_scaled = pd.DataFrame(scaled_data, columns=self.df_cleaned.columns)

        print("Scaled (Normalized) Dataset Head:")
        print(self.df_scaled.head())
        print("\nScaled Dataset Descriptive Stats (Mean should be ~0, Std Dev should be ~1):")
        print(self.df_scaled.describe())
        
        self.df_scaled.to_csv('scaled_covid_data.csv', index=False)
        
        print("-" * 40)
        return self.df_scaled

    def visualize_data(self):
        if self.df_scaled is None:
            print("Error: Data not normalized. Call normalize_data first.")
            return

        print("--- 5. Visualization Tasks ---")
        
        sns.set_style("whitegrid")
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        fig.suptitle('Confirmed and New Cases Distribution (Before and After Normalization)', fontsize=16)

        sns.histplot(self.df_cleaned['Confirmed'], kde=True, ax=axes[0, 0], color='skyblue', bins=15)
        axes[0, 0].set_title('Confirmed Cases (Cleaned - Before Norm)')
        
        sns.histplot(self.df_cleaned['New cases'], kde=True, ax=axes[0, 1], color='coral', bins=15)
        axes[0, 1].set_title('New Cases (Cleaned - Before Norm)')

        sns.histplot(self.df_scaled['Confirmed'], kde=True, ax=axes[1, 0], color='skyblue', bins=15)
        axes[1, 0].set_title('Confirmed Cases (Scaled - After Norm)')
        
        sns.histplot(self.df_scaled['New cases'], kde=True, ax=axes[1, 1], color='coral', bins=15)
        axes[1, 1].set_title('New Cases (Scaled - After Norm)')

        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.savefig('/Users/sivakumarparamasivam/Sivakumar/python_workspace/ai_engineer_2025/Python Programs/Assignments_Python/Week_6_Assignments/covid_histograms_before_after_norm.png')
        plt.close()
        print("Generated 'covid_histograms_before_after_norm.png'")

        plt.figure(figsize=(6, 5))
        
        cleaned_corr = self.df_cleaned.corr()
        
        sns.heatmap(
            cleaned_corr,
            annot=True,
            cmap='viridis',
            fmt=".2f",
            linewidths=.5,
            cbar_kws={'label': 'Correlation Coefficient'}
        )
        plt.title('Correlation Heatmap (Confirmed vs. New Cases - Cleaned Data)', fontsize=12)
        plt.savefig('/Users/sivakumarparamasivam/Sivakumar/python_workspace/ai_engineer_2025/Python Programs/Assignments_Python/Week_6_Assignments/covid_correlation_heatmap.png')
        plt.close()
        print("Generated 'covid_correlation_heatmap.png'")
        print("-" * 40)
        
    def run_all(self):
        self.load_and_select_data()
        self.compute_stats()
        self.remove_outliers_iqr()
        self.normalize_data()
        self.visualize_data()

# Instantiate and run the analysis
if __name__ == '__main__':
    eda = CovidEDA('country_wise_latest.csv')
    eda.run_all()