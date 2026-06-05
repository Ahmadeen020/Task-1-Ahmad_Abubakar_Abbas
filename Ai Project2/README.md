Data Classification Using AI

DecodeLabs Internship Project 2

### Project Overview

This project demonstrates a basic Machine Learning classification workflow using the Iris Flower Dataset. The goal is to train a model that can accurately classify iris flowers into their respective species based on flower measurements.

---

## Objectives

* Load and understand a dataset
* Perform data preprocessing
* Split data into training and testing sets
* Apply a classification algorithm
* Evaluate model performance
* Save the trained model for future use

---

## Dataset

The Iris Dataset is a well-known machine learning dataset containing 150 flower samples.

### Features

1. Sepal Length
2. Sepal Width
3. Petal Length
4. Petal Width

### Target Classes

* Setosa
* Versicolor
* Virginica

---

## Technologies Used

* Python
* Scikit-Learn
* Joblib

---

## Machine Learning Workflow

### 1. Data Loading

The Iris dataset is loaded from Scikit-Learn.

### 2. Data Splitting

The dataset is divided into:

* 80% Training Data
* 20% Testing Data

### 3. Feature Scaling

StandardScaler is used to normalize feature values.

### 4. Model Training

A Logistic Regression classifier is trained using the scaled training data.

### 5. Model Evaluation

The model is evaluated using:

* Accuracy Score
* Confusion Matrix
* F1 Score
* Classification Report

### 6. Model Saving

The trained model and scaler are saved using Joblib.

---

## Expected Output

The program displays:

* Dataset information
* Accuracy score
* F1 score
* Confusion matrix
* Classification report
* Example predictions

---

## Author

Ahmad Abubakar Abbas

DecodeLabs Artificial Intelligence Internship 2026
