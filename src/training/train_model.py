import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


df = pd.read_csv("../data/processed/final_diabetes.csv")

print("Dataset Loaded")

# FEATURES & TARGET

X = df.drop("diabetes", axis=1)

y = df["diabetes"]

# TRAIN TEST SPLIT

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Train Test Split Done")

# FEATURE SCALING

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)

# Save scaler
joblib.dump(
    scaler,
    "../models/scaler.pkl"
)

print("Scaler Saved")

# MODEL CREATION

model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    random_state=42
)

# TRAIN MODEL

model.fit(X_train, y_train)

print("Model Training Completed")

# PREDICTIONS

y_pred = model.predict(X_test)

# EVALUATION

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy Score:")
print(accuracy)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# SAVE MODEL

joblib.dump(
    model,
    "../models/diabetes_model.pkl"
)

print("\nModel Saved Successfully")