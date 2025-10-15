import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.linear_model import ElasticNet
import mlflow

# ... imports for custom config, model saving, etc.

class ModelTrainer:
    def __init__(self, config):
        self.config = config
        
    def eval_metrics(self, actual, pred):
        # Calculate evaluation metrics
        rmse = mean_squared_error(actual, pred, squared=False)
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2

    def train(self, data_path):
        data = pd.read_csv(data_path)
        
        # Split data (assuming transformation handles this)
        train_x, test_x, train_y, test_y = train_test_split(...)
        
        # Set MLflow tracking URI (e.g., pointing to Dagshub or a remote server)
        mlflow.set_tracking_uri(self.config.mlflow_uri) 
        mlflow.set_experiment(self.config.experiment_name)

        with mlflow.start_run():
            lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio)
            lr.fit(train_x, train_y)
            
            predicted_qualities = lr.predict(test_x)
            (rmse, mae, r2) = self.eval_metrics(test_y, predicted_qualities)
            
            # Log parameters, metrics, and model with MLflow
            mlflow.log_param("alpha", self.config.alpha)
            mlflow.log_param("l1_ratio", self.config.l1_ratio)
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)

            mlflow.sklearn.log_model(lr, "model")
            
            # Save the model locally for later deployment
            # ... model saving logic ...
