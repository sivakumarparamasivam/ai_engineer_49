import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

class HousePricePredicton:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
        self.df_selected = None
        self.df_cleaned = None
        self.df_scaled = None

    def load_and_select_data(self):
        self.data = pd.read_csv(self.file_path)
        cols_to_keep = ['Square_Footage', 'House_Price']
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

        outlier_mask_confirmed = iqr_outlier_remover(df['Square_Footage'])
        outlier_mask_newcases = iqr_outlier_remover(df['House_Price'])

        combined_mask = outlier_mask_confirmed & outlier_mask_newcases
        
        self.df_cleaned = df[combined_mask] 

        # testing

        print(f"Original shape: {df.shape}")
        print(f"Cleaned shape (after removing {df.shape[0] - self.df_cleaned.shape[0]} rows): {self.df_cleaned.shape}")

        print("\nCleaned Dataset Head:")
        print(self.df_cleaned.head())
        print("\nCleaned Dataset Descriptive Stats:")
        print(self.df_cleaned.describe())
        
        self.df_cleaned.to_csv('/Users/sivakumarparamasivam/Sivakumar/python_workspace/ai_engineer_2025/Python Programs/Assignments_Python/Week_7_Assignments_18th_Oct/house_price_data_cleaned.csv', index=False)
        
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
        
        self.df_scaled.to_csv('/Users/sivakumarparamasivam/Sivakumar/python_workspace/ai_engineer_2025/Python Programs/Assignments_Python/Week_7_Assignments_18th_Oct/scaled_houseprice_data.csv', index=False)
        
        print("-" * 40)
        return self.df_scaled

    def visualize_data(self):
        if self.df_cleaned is None:
            print("Error: Data not cleaned. Call remove_outliers_iqr first.")
            return  # <-- this return is now inside the if block

        print("--- 5. Visualization: Relationship between Square Footage and Price ---")
    
        plt.figure(figsize=(8, 6))
        sns.scatterplot(
            x='Square_Footage',
            y='House_Price',
            data=self.df_cleaned,
            alpha=0.7,
            color='teal'
    )
        plt.title('Relationship between Square Footage and House Price', fontsize=14)
        plt.xlabel('Square Footage')
        plt.ylabel('House Price')
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.show()

    def train_test(self):
        if self.df_cleaned is None:
            print("Error: Data not cleaned. Call remove_outliers_iqr() first.")
            return
        
        print("--- 6. Train/Test Split and Linear Regression ---")

        # ✅ Define X and y as class attributes (so other methods can use them)
        self.X = self.df_cleaned[['Square_Footage']]
        self.y = self.df_cleaned['House_Price']

        # Split data into training/testing sets
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)

        # Train model
        model = LinearRegression()
        model.fit(X_train, y_train)

        # ✅ Predict and store in self.y_pred for later plotting
        self.y_pred = model.predict(X_test)

        # Print coefficients
        print(f"Intercept (b₀): {model.intercept_:.2f}")
        print(f"Coefficient (b₁): {model.coef_[0]:.2f}")

        # ✅ Calculate performance metrics
        mse = mean_squared_error(y_test, self.y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, self.y_pred)

        print(f"\nMean Squared Error (MSE): {mse:.2f}")
        print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
        print(f"R² Score: {r2:.4f}")

        # Store model and test data for later visualization
        self.model = model
        self.X_test, self.y_test = X_test, y_test

        

    def plot_line_actual_vs_predicted(self):
        if not hasattr(self, 'y_pred'):
            print("Error: Run train_test() before plotting.")
            return

        # Regression Line Visualization
        plt.figure(figsize=(8,6))
        sns.scatterplot(x=self.X_test.squeeze(), y=self.y_test, color='teal', alpha=0.7, label='Actual Data')
        plt.plot(self.X_test, self.y_pred, color='orange', linewidth=2, label='Regression Line')
        plt.title('Regression Line vs Actual Data')
        plt.xlabel('Square Footage')
        plt.ylabel('House Price')
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.show()

        # Actual vs Predicted Visualization
        plt.figure(figsize=(7,6))
        sns.scatterplot(x=self.y_test, y=self.y_pred, color='purple', alpha=0.7)
        plt.plot([self.y_test.min(), self.y_test.max()], [self.y_test.min(), self.y_test.max()], 'r--', lw=2, label='Perfect Prediction')
        plt.title('Actual vs Predicted Prices')
        plt.xlabel('Actual')
        plt.ylabel('Predicted')
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.show()

    def predict_user_input(self):
        if not hasattr(self, 'model'):
            print("Error: Model not trained. Run train_test() first.")
            return
        
        try:
            # Get input from user
            user_input = float(input("Enter the Square Footage of the house: "))

            # Reshape input (model expects 2D array)
            user_data = np.array([[user_input]])

            # Predict using trained model
            predicted_price = self.model.predict(user_data)[0]

            print(f"Predicted House Price for {user_input:.2f} sqft: ${predicted_price:,.2f}")

        except ValueError:
            print("Invalid input. Please enter a numeric value.")


    
        
    def run_all(self):
        self.load_and_select_data()
        self.compute_stats()
        self.remove_outliers_iqr()
        self.normalize_data()
        self.visualize_data()
        self.train_test()
        self.plot_line_actual_vs_predicted()
        self.predict_user_input()

# Instantiate and run the analysis
if __name__ == '__main__':
    eda = HousePricePredicton('/Users/sivakumarparamasivam/Sivakumar/python_workspace/ai_engineer_2025/Python Programs/Assignments_Python/Week_7_Assignments_18th_Oct/house_price_regression_dataset.csv')
    eda.run_all()