from typing import Optional, List
import pandas as pd
import numpy as np

class DataCleaner:
    """Basic data cleaning operations"""
    
    def __init__(self, data: pd.DataFrame):
        self.data = data.copy()
    
    def handle_missing_values(self, columns: Optional[List[str]] = None) -> pd.DataFrame:
        """Handle missing values by dropping them"""
        target_cols = columns if columns else self.data.columns
        before_rows = len(self.data)
        self.data = self.data.dropna(subset=target_cols)
        print(f"Dropped {before_rows - len(self.data)} rows with missing values")
        return self.data

    def remove_duplicates(self) -> pd.DataFrame:
        """Remove duplicate rows from the dataset"""
        before_rows = len(self.data)
        self.data = self.data.drop_duplicates()
        print(f"Removed {before_rows - len(self.data)} duplicate rows")
        return self.data