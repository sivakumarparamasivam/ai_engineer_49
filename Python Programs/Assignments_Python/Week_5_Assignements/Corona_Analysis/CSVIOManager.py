import os
import pandas as pd
from datetime import datetime

class CSVManager:
    def read_csv(self, filepath: str, **kwargs) -> pd.DataFrame:
        """Read CSV file and return DataFrame"""
        try:
            df = pd.read_csv(filepath, **kwargs)
            print(f"Successfully read CSV file with {len(df)} rows and {len(df.columns)} columns")
            return df
        except Exception as e:
            print(f"Error reading CSV file: {str(e)}")
            raise

    def write_csv(self, df: pd.DataFrame, filepath: str, **kwargs):
        """Write DataFrame to CSV file"""
        try:
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(filepath) if os.path.dirname(filepath) else '.', exist_ok=True)
            
            # Write DataFrame to CSV
            df.to_csv(filepath, index=False, **kwargs)
            print(f"Successfully wrote data to {filepath}")
            print(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns")
        except Exception as e:
            print(f"Error writing CSV file: {str(e)}")
            raise