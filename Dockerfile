# Use the official Python base image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the MLflow model artifacts
COPY . /app

# Install dependencies
RUN pip install mlflow

# Expose the port MLflow will run on
EXPOSE 5000

# Command to run the MLflow model server
CMD ["mlflow", "models", "serve", "-m", "models:/logistic_model_v1/1", "-p", "5000"]
