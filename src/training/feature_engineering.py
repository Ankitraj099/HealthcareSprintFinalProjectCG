import pandas as pd
import joblib

from sklearn.preprocessing import LabelEncoder


df = pd.read_csv("../data/processed/cleaned_diabetes.csv")

print("Dataset Loaded")

# ENCODE CATEGORICAL FEATURES

gender_encoder = LabelEncoder()
smoking_encoder = LabelEncoder()

df['gender'] = gender_encoder.fit_transform(df['gender'])

df['smoking_history'] = smoking_encoder.fit_transform(
    df['smoking_history']
)

# SAVE ENCODERS

joblib.dump(
    gender_encoder,
    "../models/gender_encoder.pkl"
)

joblib.dump(
    smoking_encoder,
    "../models/smoking_encoder.pkl"
)

print("Encoders Saved")

# SAVE FINAL DATASET

FINAL_DATA_PATH = "../data/processed/final_diabetes.csv"

df.to_csv(FINAL_DATA_PATH, index=False)

print("Feature Engineering Completed")
print(f"Final Dataset Saved At: {FINAL_DATA_PATH}")