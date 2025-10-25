import pandas as pd
import numpy as np
from dataset import DatasetLoader
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

class CleanedData(DatasetLoader):
    def __init__(self, file_path):
        super().__init__(file_path)

    # Fill missing values with mean
    def fill_missing_values(self):
        try:
            data = self.get_data()
            data_cleaned = data.copy()

            for col in data_cleaned.select_dtypes(include=[np.number]).columns:
                mean = data_cleaned[col].mean()
                data_cleaned[col].fillna(mean, inplace=True)

        except Exception as e:
            print("Error filling missing values:", e)
        return data_cleaned

    # Remove outliers using IQR method
    def remove_outliers(self, data_cleaned, columns):
        try:
            data_outliers_removed = data_cleaned.copy()
            for column in columns:
                Q1 = data_outliers_removed[column].quantile(0.25)
                Q3 = data_outliers_removed[column].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR

                outliers = data_outliers_removed[(data_outliers_removed[column] < lower_bound) | (data_outliers_removed[column] > upper_bound)]
                data_outliers_removed.drop(outliers.index, inplace=True)

        except Exception as e:
            print("Error removing outliers:", e)
        return data_outliers_removed
    
    # train and test with SciKit Learn
    def Split_Train(data):
        try:
            X = data[['Module_Complexity_Score',
                       'Test_Case_Count',
                       'Automation_Coverage',
                       'Code_Churn',
            'Defects_Previous_Cycle',
            'Execution_Time_Previous']]

         
            y = data[['Estimated_Execution_Time', 'Expected_Defect_Count']]

            # Train/Test Split
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
        )

            # Train model
            model = LinearRegression()
            model.fit(X_train, y_train)

            # Predict
            y_pred = model.predict(X_test)

           
            y_pred_df = pd.DataFrame(
                y_pred,
                columns=['Predicted_Estimated_Execution_Time', 'Predicted_Expected_Defect_Count']
            )

           
            X_test_reset = X_test.reset_index(drop=True)
            y_test_reset = y_test.reset_index(drop=True)
            y_pred_df_reset = y_pred_df.reset_index(drop=True)

           
            final_result = pd.concat([X_test_reset, y_test_reset, y_pred_df_reset], axis=1)

            
            pd.set_option('display.max_columns', None)   # show all columns
            pd.set_option('display.width', 2000)         # prevent line wrapping
            print(final_result.head(20))  # show first 20 rows

            # 📝 Write to Excel file
            final_result.to_excel('regression_results.xlsx', index=False)

            print("\n✅ Results saved to 'regression_results.xlsx'")
        except Exception as e:
            print("Error in training and testing the model:", e)

if __name__ == "__main__":
    read_file_path = 'data/qa_regression_raw_dataset.csv'
    write_file_path = 'data/qa_regression_cleaned_dataset.csv'
    cleaner = CleanedData(read_file_path)
    data = cleaner.get_data()
    print("Loaded data successfully.\n")

    cleaned_data = cleaner.fill_missing_values()
    print("Completed filling missing values.\n")

    columns = ['Test_Case_Count', 'Code_Churn', 'Execution_Time_Previous']
    cleaned_data = cleaner.remove_outliers(cleaned_data, columns)
    print("Completed removing outliers.\n")

    cleaner.set_data(cleaned_data, write_file_path)
    print("Cleaned data saved successfully.\n")

    predictions = CleanedData.Split_Train(cleaned_data)
    print("Predictions from the model:\n", predictions)
