import pandas as pd
import numpy as np
from typing import Optional, List, Dict, Any, Union

class DataAnalysis:
    """Comprehensive data analysis operations"""
    
    def __init__(self, data: pd.DataFrame):
        self.data = data
        self.results: Dict[str, Any] = {}
    
    def descriptive_statistics(self, columns: Optional[List[str]] = None) -> pd.DataFrame:
        """Get descriptive statistics"""
        cols = columns if columns else self.data.select_dtypes(include=[np.number]).columns
        stats = self.data[cols].describe()
        self.results['descriptive_stats'] = stats
        
        print("\n" + "="*70)
        print("DESCRIPTIVE STATISTICS")
        print("="*70)
        print(stats)
        print("="*70)
        
        return stats
    
    def correlation_analysis(self, columns: Optional[List[str]] = None, 
                           method: str = 'pearson') -> pd.DataFrame:
        """Calculate correlation matrix"""
        cols = columns if columns else self.data.select_dtypes(include=[np.number]).columns
        corr = self.data[cols].corr(method=method)
        self.results['correlation'] = corr
        
        print("\n" + "="*70)
        print(f"CORRELATION MATRIX ({method.upper()})")
        print("="*70)
        print(corr)
        print("="*70)
        
        return corr
    
    def group_analysis(self, groupby_col: Union[str, List[str]], 
                      agg_dict: Dict[str, Union[str, List[str]]]) -> pd.DataFrame:
        """Perform group-by analysis"""
        grouped = self.data.groupby(groupby_col).agg(agg_dict).reset_index()
        self.results['grouped_analysis'] = grouped
        
        print("\n" + "="*70)
        print(f"GROUP ANALYSIS BY: {groupby_col}")
        print("="*70)
        print(grouped.head(20))
        print("="*70)
        
        return grouped
    
    def value_counts(self, column: str, top_n: Optional[int] = None, 
                    normalize: bool = False) -> pd.Series:
        """Get value counts for a column"""
        counts = self.data[column].value_counts(normalize=normalize)
        if top_n:
            counts = counts.head(top_n)
        
        self.results[f'value_counts_{column}'] = counts
        
        print("\n" + "="*70)
        print(f"VALUE COUNTS: {column}" + (" (Normalized)" if normalize else ""))
        print("="*70)
        print(counts)
        print("="*70)
        
        return counts
    
    def missing_value_analysis(self) -> pd.DataFrame:
        """Analyze missing values"""
        missing = pd.DataFrame({
            'Column': self.data.columns,
            'Missing_Count': self.data.isnull().sum().values,
            'Missing_Percentage': (self.data.isnull().sum() / len(self.data) * 100).values
        })
        missing = missing[missing['Missing_Count'] > 0].sort_values('Missing_Count', ascending=False)
        
        self.results['missing_analysis'] = missing
        
        print("\n" + "="*70)
        print("MISSING VALUE ANALYSIS")
        print("="*70)
        if len(missing) == 0:
            print("No missing values found!")
        else:
            print(missing.to_string(index=False))
        print("="*70)
        
        return missing
    
    def outlier_detection(self, columns: List[str], 
                         method: str = 'iqr',
                         threshold: float = 1.5) -> Dict[str, pd.DataFrame]:
        """Detect outliers in specified columns"""
        outliers = {}
        
        for col in columns:
            if col not in self.data.columns or not pd.api.types.is_numeric_dtype(self.data[col]):
                continue
            
            if method == 'iqr':
                Q1 = self.data[col].quantile(0.25)
                Q3 = self.data[col].quantile(0.75)
                IQR = Q3 - Q1
                lower = Q1 - threshold * IQR
                upper = Q3 + threshold * IQR
                outlier_mask = (self.data[col] < lower) | (self.data[col] > upper)
            
            elif method == 'zscore':
                mean = self.data[col].mean()
                std = self.data[col].std()
                z_scores = np.abs((self.data[col] - mean) / std)
                outlier_mask = z_scores > threshold
            
            outlier_data = self.data[outlier_mask].copy()
            outliers[col] = outlier_data
            
            print(f"\n{'='*70}")
            print(f"OUTLIERS IN: {col} (Method: {method.upper()})")
            print(f"{'='*70}")
            print(f"Total Outliers: {len(outlier_data)}")
            print(f"Percentage: {len(outlier_data)/len(self.data)*100:.2f}%")
            if len(outlier_data) > 0:
                print(f"\nSample Outliers:")
                print(outlier_data.head(10)[[col]])
            print(f"{'='*70}")
        
        self.results['outliers'] = outliers
        return outliers
    
    def summary_report(self) -> str:
        """Generate comprehensive summary report"""
        report = "\n" + "="*70 + "\n"
        report += "COMPREHENSIVE DATA ANALYSIS REPORT\n"
        report += "="*70 + "\n\n"
        
        # Basic info
        report += f"Dataset Shape: {self.data.shape[0]} rows × {self.data.shape[1]} columns\n"
        report += f"Memory Usage: {self.data.memory_usage(deep=True).sum() / 1024**2:.2f} MB\n\n"
        
        # Column types
        report += "Column Types:\n"
        report += "-"*70 + "\n"
        type_counts = self.data.dtypes.value_counts()
        for dtype, count in type_counts.items():
            report += f"  {dtype}: {count} columns\n"
        
        # Missing values
        total_missing = self.data.isnull().sum().sum()
        report += f"\nTotal Missing Values: {total_missing}\n"
        
        # Numeric columns summary
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns
        report += f"\nNumeric Columns: {len(numeric_cols)}\n"
        
        # Categorical columns summary
        cat_cols = self.data.select_dtypes(include=['object', 'category']).columns
        report += f"Categorical Columns: {len(cat_cols)}\n"
        
        report += "\n" + "="*70 + "\n"
        
        return report