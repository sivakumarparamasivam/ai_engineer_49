import os
import pandas as pd
import numpy as np
from typing import Optional, Dict, Any, List
from datetime import datetime
from Visualization import DataVisualization

from CSVIOManager import CSVManager
from DataCleaner import DataCleaner
from DataAnalysis import DataAnalysis

class CovidAnalysisPipeline:
    """Complete COVID-19 analysis pipeline with all features"""
    
    def __init__(self):
        self.csv_manager = CSVManager()
        self.data: Optional[pd.DataFrame] = None
        self.cleaner: Optional[DataCleaner] = None
        self.analyzer: Optional[DataAnalysis] = None
        self.visualizer: Optional[DataVisualization] = None
        self.results: Dict[str, Any] = {}
        
        # Create output directories
        os.makedirs('visualizations', exist_ok=True)
        os.makedirs('results', exist_ok=True)
    
    def load_csv(self, filepath: str, **kwargs) -> 'CovidAnalysisPipeline':
        """Load CSV data"""
        try:
            self.data = self.csv_manager.read_csv(filepath, **kwargs)
            print(f"Successfully loaded DataFrame with shape: {self.data.shape}")
            return self
        except Exception as e:
            print(f"Error loading CSV: {str(e)}")
            raise
    
    def save_csv(self, filepath: str, data: Optional[pd.DataFrame] = None, **kwargs):
        """Save data to CSV"""
        save_data = data if data is not None else self.data
        self.csv_manager.write_csv(save_data, filepath, **kwargs)
        return self
    
    def initialize_components(self):
        """Initialize all components after data is loaded"""
        if self.data is None:
            raise ValueError("No data loaded. Call load_csv() first.")
        
        self.cleaner = DataCleaner(self.data)
        self.analyzer = DataAnalysis(self.data)
        self.visualizer = DataVisualization(self.data)
        return self
    
    def run_analysis(self):
        """Run the complete analysis pipeline"""
        if self.data is None:
            raise ValueError("No data loaded. Call load_csv() first.")
        
        # Initialize components if not already done
        if any(x is None for x in [self.cleaner, self.analyzer, self.visualizer]):
            self.initialize_components()
        
        # Create visualizations directory
        viz_dir = os.path.join(os.getcwd(), 'visualizations')
        os.makedirs(viz_dir, exist_ok=True)
        
        # 1. Basic statistics
        print("\nBasic Statistics:")
        print("-" * 80)
        print(self.data.describe())
        
        # 2. Regional analysis
        print("\nRegional Analysis:")
        print("-" * 80)
        regional_summary = self.data.groupby('WHO Region').agg({
            'Confirmed': 'sum',
            'Deaths': 'sum',
            'Recovered': 'sum',
            'Active': 'sum'
        }).round(2)
        print(regional_summary)
        
        # 3. Create visualizations
        # Confirmed cases by region
        self.visualizer.plot_bar_chart(
            x='WHO Region',
            y='Confirmed',
            save_path=os.path.join(viz_dir, 'confirmed_by_region.png')
        )
        
        # Top 10 countries by confirmed cases
        top10_data = self.data.nlargest(10, 'Confirmed')
        self.visualizer.plot_bar_chart(
            x='Country/Region',
            y='Confirmed',
            save_path=os.path.join(viz_dir, 'top10_countries.png')
        )
        
        # Death rate analysis
        self.data['Death_Rate'] = (self.data['Deaths'] / self.data['Confirmed'] * 100).round(2)
        self.visualizer.plot_bar_chart(
            x='Country/Region',
            y='Death_Rate',
            save_path=os.path.join(viz_dir, 'death_rates.png')
        )
        
        # Recovery rate analysis
        self.data['Recovery_Rate'] = (self.data['Recovered'] / self.data['Confirmed'] * 100).round(2)
        self.visualizer.plot_bar_chart(
            x='Country/Region',
            y='Recovery_Rate',
            save_path=os.path.join(viz_dir, 'recovery_rates.png')
        )
        
        # Correlation heatmap
        numeric_cols = ['Confirmed', 'Deaths', 'Recovered', 'Active', 'Death_Rate', 'Recovery_Rate']
        self.visualizer.plot_correlation_heatmap(
            columns=numeric_cols,
            save_path=os.path.join(viz_dir, 'correlation_heatmap.png')
        )
        
        print("\nAnalysis complete! Visualizations have been saved to:", viz_dir)
        return self.data

if __name__ == "__main__":
    try:
        # Initialize pipeline
        pipeline = CovidAnalysisPipeline()
        
        # Load and analyze data
        data_path = "/Users/sivakumarparamasivam/Sivakumar/python_workspace/ai_engineer_2025/Python Programs/Assignments_Python/Week_5_Assignements/Corona_Analysis/country_wise_latest.csv"
        
        if not os.path.exists(data_path):
            raise FileNotFoundError(f"Data file not found: {data_path}")
        
        print(f"Loading data from: {data_path}")
        pipeline.load_csv(data_path)
        
        if pipeline.data is None:
            raise ValueError("Failed to load data")
            
        print("Initializing components...")
        pipeline.initialize_components()
        
        print("Running analysis...")
        pipeline.run_analysis()
        
    except Exception as e:
        print(f"Error: {str(e)}")