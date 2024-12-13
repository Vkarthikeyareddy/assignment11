import mlflow
import mlflow.sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load and split data
data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Log the model with MLflow
mlflow.sklearn.log_model(model, "logistic_regression_model", registered_model_name="logistic_model_v1")
print("Model logged successfully!")
