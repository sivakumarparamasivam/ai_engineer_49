import os
import pandas as pd
from CSVIOManager import CSVManager
from DataCleaner import DataCleaner
from DataAnalysis import DataAnalysis
from Visualization import DataVisualization

class CovidAnalysisPipeline:
    """Simplified COVID-19 analysis pipeline"""
    
    def __init__(self):
        """Initialize the pipeline"""
        self.csv_manager = CSVManager()
        self.data = None
        self.cleaner = None
        self.analyzer = None
        self.visualizer = None
        
        # Create visualization directory
        os.makedirs('visualization', exist_ok=True)
    
    def load_data(self, filepath: str) -> 'CovidAnalysisPipeline':
        """Load and prepare the COVID-19 data"""
        try:
            # Load data
            self.data = self.csv_manager.read_csv(filepath)
            
            # Initialize components
            self.cleaner = DataCleaner(self.data)
            self.analyzer = DataAnalysis(self.data)
            self.visualizer = DataVisualization(self.data)
            
            # Clean data
            self.data = self.cleaner.handle_missing_values()
            self.data = self.cleaner.remove_duplicates()
            return self
            
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            raise
    
    def run_analysis(self) -> 'CovidAnalysisPipeline':
        """Run the complete analysis pipeline"""
        try:
            if self.data is None:
                raise ValueError("No data loaded. Call load_data() first.")
                
            # Calculate statistics and rates
            self.analyzer.descriptive_statistics()
            self.analyzer.correlation_analysis()
            self.analyzer.calculate_recovery_rate()
            self.analyzer.calculate_death_rate()
            
            # Create visualizations
            self.visualizer.plot_top_countries(save_path='visualization/top10_countries_confirmed.png')
            self.visualizer.plot_correlation_heatmap(save_path='visualization/correlation_heatmap.png')
            self.visualizer.plot_deaths_by_region(save_path='visualization/deaths_by_region_pie.png')
            self.visualizer.plot_recovery_rates(save_path='visualization/top10_recovery_rate.png')
            
            # Save processed data
            self.csv_manager.write_csv(self.data, 'visualization/covid_analysis_results.csv')
            return self
            
        except Exception as e:
            print(f"Error in analysis: {str(e)}")
            raise

if __name__ == "__main__":
    try:
        # Create and run the pipeline
        pipeline = CovidAnalysisPipeline()
        pipeline.load_data("./country_wise_latest.csv")
        pipeline.run_analysis()
        print("Analysis completed successfully!")
        
    except Exception as e:
        print(f"Pipeline execution failed: {str(e)}")
        exit(1)