import pandas as pd
import yaml
# ... import custom config and schema classes

class DataValidation:
    def __init__(self, config):
        self.config = config
        self.schema = yaml.safe_load(Path(self.config.schema_path).read_text())
        
    def validate_columns(self, data_path):
        data = pd.read_csv(data_path)
        validation_status = True

        # 1. Check if all required columns are present
        if list(data.columns) != list(self.schema['columns'].keys()):
            validation_status = False

        # 2. Check data types
        for col, dtype in self.schema['columns'].items():
            if str(data[col].dtype) != dtype:
                validation_status = False
                
        # 3. URL Check Output/Logging (simulated)
        with open(self.config.status_file, 'w') as f:
            f.write(f"Data Validation Status: {validation_status}")
        
        return validation_status
