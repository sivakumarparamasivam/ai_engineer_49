import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

class DataVisualization:
    """Basic visualization tools for COVID-19 data analysis"""
    
    def __init__(self, data: pd.DataFrame):
        self.data = data
        self._setup_style()
    
    def _setup_style(self):
        """Setup basic plot style"""
        plt.style.use('seaborn-v0_8-darkgrid')
        plt.rcParams['figure.figsize'] = (12, 6)
        plt.rcParams['font.size'] = 10
    
    def plot_top_countries(self, metric: str = 'Confirmed', top_n: int = 10, save_path: str = None):
        """Plot top N countries by given metric"""
        plt.figure(figsize=(12, 6))
        data = self.data.nlargest(top_n, metric)
        sns.barplot(x=metric, y='Country/Region', data=data)
        plt.title(f'Top {top_n} Countries by {metric} Cases')
        
        if save_path:
            plt.savefig(save_path)
            print(f"Saved plot to {save_path}")
        plt.close()
    
    def plot_correlation_heatmap(self, save_path: str = None):
        """Plot correlation heatmap of main metrics"""
        plt.figure(figsize=(10, 8))
        corr = self.data[['Confirmed', 'Deaths', 'Recovered']].corr()
        sns.heatmap(corr, annot=True, cmap='coolwarm')
        plt.title('Correlation between COVID-19 Metrics')
        
        if save_path:
            plt.savefig(save_path)
            print(f"Saved plot to {save_path}")
        plt.close()
    
    def plot_deaths_by_region(self, save_path: str = None):
        """Plot pie chart of deaths by region"""
        plt.figure(figsize=(12, 8))
        deaths_by_region = self.data.groupby('WHO Region')['Deaths'].sum()
        plt.pie(deaths_by_region, labels=deaths_by_region.index, autopct='%1.1f%%')
        plt.title('Distribution of Deaths by Region')
        
        if save_path:
            plt.savefig(save_path)
            print(f"Saved plot to {save_path}")
        plt.close()
    
    def plot_recovery_rates(self, top_n: int = 10, save_path: str = None):
        """Plot recovery rates for top N countries"""
        plt.figure(figsize=(12, 6))
        recovery_rates = (self.data['Recovered'] / self.data['Confirmed'] * 100).round(2)
        self.data['Recovery_Rate'] = recovery_rates
        data = self.data.nlargest(top_n, 'Recovery_Rate')
        
        sns.barplot(x='Recovery_Rate', y='Country/Region', data=data)
        plt.title(f'Top {top_n} Countries by Recovery Rate')
        
        if save_path:
            plt.savefig(save_path)
            print(f"Saved plot to {save_path}")
        plt.close()