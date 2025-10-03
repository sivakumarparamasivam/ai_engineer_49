import datetime
import os
from typing import Dict, List
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class CSVManager:
    def __init__(self):
        self.file_history:List[Dict] = []

    def read_csv(self, filepath:str, **kwargs) -> pd.DataFrame:
        default_params = {
            'encoding':'utf-8'
        }

        default_params.update(kwargs)

        try:
            print(f"Attempting to read CSV file: {filepath}")
            df = pd.read_csv(filepath, **default_params)
            print(f"Successfully read CSV file with {len(df)} rows and {len(df.columns)} columns")
            self.file_history.append({
                'action': 'read',
                'filepath': filepath,
                'timestamp': datetime.datetime.now(),
                'rows': len(df),
                'columns': len(df.columns)
            })
            return df
        except Exception as e:
            raise IOError(f"Error reading CSV: {str(e)}")    

    def write_csv(self, df:pd.DataFrame, filepath:str, **kwargs) -> pd.DataFrame:
        default_params = {
            'index': False,
            'encoding':'utf-8'
        }

        default_params.update(kwargs)

        try:
            df = pd.read_csv(filepath, **default_params)
            self.file_history.append({})
        except Exception as e:
            raise IOError(f"Error reading CSV: {str(e)}")
        
        try:
            os.makedirs(os.path.dirname(filepath) if os.path.dirname(filepath) else '.', exist_ok=True)
            
            df.to_csv(filepath, **default_params)
            self.file_history.append({
                'action': 'write',
                'filepath': filepath,
                'timestamp': datetime.now(),
                'rows': len(df),
                'columns': len(df.columns)
            })
            print(f"✓ Saved: {filepath}")
            print(f"  Shape: {df.shape[0]} rows × {df.shape[1]} columns")
        except Exception as e:
            raise IOError(f"Error writing CSV: {str(e)}")