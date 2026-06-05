# Data Classification Using AI - DecodeLabs Internship Project 2

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
accuracy_score,
confusion_matrix,
classification_report,
f1_score
)
import os
import joblib
#LOAD DATASET

iris = load_iris()

X = iris.data
y = iris.target

print("=" * 50)
print("IRIS DATASET LOADED SUCCESSFULLY")
print("=" * 50)

print(f"Number of Samples: {X.shape[0]}")
print(f"Number of Features: {X.shape[1]}")
print(f"Target Classes: {iris.target_names}")

#SPLIT DATASET

X_train, X_test, y_train, y_test = train_test_split(
X,
y,
test_size=0.2,
random_state=42
)

#FEATURE SCALING


scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


#TRAIN MODEL


model = LogisticRegression(max_iter=200)

model.fit(X_train_scaled, y_train)


# MAKE PREDICTIONS


y_pred = model.predict(X_test_scaled)


# EVALUATE MODEL


accuracy = accuracy_score(y_test, y_pred)

cm = confusion_matrix(y_test, y_pred)

f1 = f1_score(
y_test,
y_pred,
average="weighted"
)

print("\n" + "=" * 50)
print("MODEL EVALUATION")
print("=" * 50)

print(f"Accuracy Score: {accuracy:.4f}")
print(f"F1 Score: {f1:.4f}")

print("\nConfusion Matrix:")
print(cm)

print("\nClassification Report:")
print(classification_report(
y_test,
y_pred,
target_names=iris.target_names
))


# SAMPLE PREDICTIONS


print("\nSample Predictions:")

for i in range(5):
 prediction = iris.target_names[y_pred[i]]
actual = iris.target_names[y_test[i]]


print(
    f"Sample {i+1}: "
    f"Predicted = {prediction} | "
    f"Actual = {actual}"
)


#SAVE MODEL

os.makedirs("models", exist_ok=True)

joblib.dump(
model,
"models/iris_logistic_regression.joblib"
)

joblib.dump(
scaler,
"models/scaler.joblib"
)

print("\nModel and Scaler saved successfully.")
print("\nProject completed successfully.")
