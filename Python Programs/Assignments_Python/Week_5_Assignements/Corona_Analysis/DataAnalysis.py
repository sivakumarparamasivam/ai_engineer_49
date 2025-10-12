import pandas as pd
import numpy as np
from typing import Optional, List

class DataAnalysis:
    """Basic data analysis operations for COVID-19 data"""
    
    def __init__(self, data: pd.DataFrame):
        self.data = data
    
    def descriptive_statistics(self) -> pd.DataFrame:
        """Calculate basic descriptive statistics for numerical columns"""
        numeric_cols = ['Confirmed', 'Deaths', 'Recovered']
        stats = self.data[numeric_cols].describe()
        print("\nDescriptive Statistics:")
        print(stats)
        return stats
    
    def correlation_analysis(self) -> pd.DataFrame:
        """Calculate correlation between confirmed cases, deaths, and recovered"""
        numeric_cols = ['Confirmed', 'Deaths', 'Recovered']
        corr = self.data[numeric_cols].corr()
        print("\nCorrelation Analysis:")
        print(corr)
        return corr
    
    def calculate_recovery_rate(self) -> pd.Series:
        """Calculate recovery rate for each country"""
        self.data['Recovery_Rate'] = (self.data['Recovered'] / self.data['Confirmed'] * 100).round(2)
        return self.data['Recovery_Rate']
    
    def calculate_death_rate(self) -> pd.Series:
        """Calculate death rate for each country"""
        self.data['Death_Rate'] = (self.data['Deaths'] / self.data['Confirmed'] * 100).round(2)
        return self.data['Death_Rate']