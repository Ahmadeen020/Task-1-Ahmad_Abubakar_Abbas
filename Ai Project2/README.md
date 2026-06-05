# Iris Classification Project

This project demonstrates a simple, fully commented workflow to train and evaluate a classifier on the Iris dataset using scikit-learn.

Files added/updated
- `classification.py`: main script that trains, evaluates, and saves the model and scaler to `models/`.
- `requirements.txt`: Python package requirements.
- `models/`: directory created at runtime to store serialized artifacts.

Setup and run (PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate
pip install -r requirements.txt
python "Ai Project2\classification.py"
```

How to load the saved model and scaler

```python
import joblib
model = joblib.load('Ai Project2/models/iris_logistic_regression.joblib')
scaler = joblib.load('Ai Project2/models/scaler.joblib')

# Example: predict for a new sample (replace values with your measurements)
sample = [[5.1, 3.5, 1.4, 0.2]]
sample_scaled = scaler.transform(sample)
print(model.predict(sample_scaled))
```

If you want, I can also:
- add a command-line interface to `classification.py` to accept custom samples
- add unit tests or a minimal runner script
- run the script here to verify installation (note: may require installing packages)
