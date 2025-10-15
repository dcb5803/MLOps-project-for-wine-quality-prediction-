import pandas as pd
from urllib import request
from pathlib import Path
from src.config.configuration import DataIngestionConfig # Custom config class

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_data(self):
        # 1. Check if file exists, else download
        if not Path(self.config.local_data_file).exists():
            # URL check is performed here during the download/retrieval
            filename, headers = request.urlretrieve(
                url = self.config.source_url,
                filename = self.config.local_data_file
            )
            # Log successful download
        
    def initiate_data_ingestion(self):
        self.download_data()
        # Optionally, unzip/process the raw data
        # Return path to raw data
        return self.config.local_data_file
