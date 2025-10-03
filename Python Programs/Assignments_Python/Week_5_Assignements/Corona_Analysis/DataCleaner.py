from typing import Any, List, Optional, Dict
import pandas as pd


class DataCleaner:
    """Comprehensive data cleaning operations"""
    
    def __init__(self, data: pd.DataFrame):
        self.data = data.copy()
        self.original_data = data.copy()
        self.cleaning_log: List[str] = []
    
    def handle_missing_values(self, strategy: str = 'drop', 
                             fill_value: Any = None,
                             columns: Optional[List[str]] = None) -> 'DataCleaner':
        """
        Handle missing values with various strategies
        
        Args:
            strategy: 'drop', 'fill', 'mean', 'median', 'mode', 'forward', 'backward'
            fill_value: Custom fill value (for 'fill' strategy)
            columns: Specific columns to process (None = all columns)
        """
        before_rows = len(self.data)
        target_cols = columns if columns else self.data.columns
        
        if strategy == 'drop':
            self.data = self.data.dropna(subset=target_cols)
            self.cleaning_log.append(f"Dropped rows with missing values: {before_rows - len(self.data)} rows removed")
        
        elif strategy == 'fill':
            self.data[target_cols] = self.data[target_cols].fillna(fill_value)
            self.cleaning_log.append(f"Filled missing values with: {fill_value}")
        
        elif strategy == 'mean':
            for col in target_cols:
                if pd.api.types.is_numeric_dtype(self.data[col]):
                    self.data[col].fillna(self.data[col].mean(), inplace=True)
            self.cleaning_log.append("Filled numeric missing values with mean")
        
        elif strategy == 'median':
            for col in target_cols:
                if pd.api.types.is_numeric_dtype(self.data[col]):
                    self.data[col].fillna(self.data[col].median(), inplace=True)
            self.cleaning_log.append("Filled numeric missing values with median")
        
        elif strategy == 'mode':
            for col in target_cols:
                mode_val = self.data[col].mode()[0] if not self.data[col].mode().empty else None
                if mode_val is not None:
                    self.data[col].fillna(mode_val, inplace=True)
            self.cleaning_log.append("Filled missing values with mode")
        
        elif strategy == 'forward':
            self.data[target_cols] = self.data[target_cols].fillna(method='ffill')
            self.cleaning_log.append("Forward filled missing values")
        
        elif strategy == 'backward':
            self.data[target_cols] = self.data[target_cols].fillna(method='bfill')
            self.cleaning_log.append("Backward filled missing values")
        
        return self
    
    def remove_duplicates(self, subset: Optional[List[str]] = None, 
                         keep: str = 'first') -> 'DataCleaner':
        """Remove duplicate rows"""
        before_rows = len(self.data)
        self.data = self.data.drop_duplicates(subset=subset, keep=keep)
        removed = before_rows - len(self.data)
        self.cleaning_log.append(f"Removed {removed} duplicate rows")
        return self
    
    def remove_outliers(self, columns: List[str], 
                       method: str = 'iqr', 
                       threshold: float = 1.5) -> 'DataCleaner':
        """
        Remove outliers using IQR or Z-score method
        
        Args:
            columns: Columns to check for outliers
            method: 'iqr' or 'zscore'
            threshold: 1.5 for IQR, 3 for zscore (typical values)
        """
        before_rows = len(self.data)
        
        for col in columns:
            if col not in self.data.columns or not pd.api.types.is_numeric_dtype(self.data[col]):
                continue
            
            if method == 'iqr':
                Q1 = self.data[col].quantile(0.25)
                Q3 = self.data[col].quantile(0.75)
                IQR = Q3 - Q1
                lower = Q1 - threshold * IQR
                upper = Q3 + threshold * IQR
                self.data = self.data[(self.data[col] >= lower) & (self.data[col] <= upper)]
            
            elif method == 'zscore':
                mean = self.data[col].mean()
                std = self.data[col].std()
                z_scores = np.abs((self.data[col] - mean) / std)
                self.data = self.data[z_scores < threshold]
        
        removed = before_rows - len(self.data)
        self.cleaning_log.append(f"Removed {removed} outliers using {method} method")
        return self
    
    def standardize_columns(self, column_mapping: Dict[str, str]) -> 'DataCleaner':
        """Rename columns for standardization"""
        self.data.rename(columns=column_mapping, inplace=True)
        self.cleaning_log.append(f"Standardized {len(column_mapping)} column names")
        return self
    
    def convert_dtypes(self, type_mapping: Dict[str, str]) -> 'DataCleaner':
        """Convert column data types"""
        for col, dtype in type_mapping.items():
            if col in self.data.columns:
                try:
                    if dtype == 'datetime':
                        self.data[col] = pd.to_datetime(self.data[col])
                    else:
                        self.data[col] = self.data[col].astype(dtype)
                    self.cleaning_log.append(f"Converted {col} to {dtype}")
                except Exception as e:
                    self.cleaning_log.append(f"Failed to convert {col}: {str(e)}")
        return self
    
    def filter_rows(self, condition: str) -> 'DataCleaner':
        """Filter rows based on condition (using query syntax)"""
        before_rows = len(self.data)
        self.data = self.data.query(condition)
        removed = before_rows - len(self.data)
        self.cleaning_log.append(f"Filtered rows: {removed} removed (condition: {condition})")
        return self
    
    def reset_to_original(self) -> 'DataCleaner':
        """Reset to original data"""
        self.data = self.original_data.copy()
        self.cleaning_log.append("Reset to original data")
        return self
    
    def get_data(self) -> pd.DataFrame:
        """Return cleaned data"""
        return self.data
    
    def get_cleaning_report(self) -> str:
        """Get detailed cleaning report"""
        report = "\n" + "="*70 + "\n"
        report += "DATA CLEANING REPORT\n"
        report += "="*70 + "\n"
        report += f"Original Shape: {self.original_data.shape}\n"
        report += f"Current Shape: {self.data.shape}\n"
        report += f"Rows Removed: {len(self.original_data) - len(self.data)}\n"
        report += f"Columns: {len(self.data.columns)}\n"
        report += "\nCleaning Steps:\n"
        report += "-"*70 + "\n"
        for i, log in enumerate(self.cleaning_log, 1):
            report += f"{i}. {log}\n"
        report += "="*70 + "\n"
        return report
  