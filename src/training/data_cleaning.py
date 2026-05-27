import pandas as pd
import os

# Dataset path
DATA_PATH = "../data/raw/diabetes_prediction_dataset.csv"

# Load dataset
df = pd.read_csv(DATA_PATH)

print("Dataset Loaded Successfully")
print("Initial Shape:", df.shape)

# CHECK NULL VALUES

print("\nMissing Values:")
print(df.isnull().sum())

# REMOVE DUPLICATES

before = df.shape[0]

df.drop_duplicates(inplace=True)

after = df.shape[0]

print(f"\nDuplicates Removed: {before - after}")

# HANDLE MISSING VALUES

numerical_cols = [
    'age',
    'bmi',
    'HbA1c_level',
    'blood_glucose_level'
]

for col in numerical_cols:
    df[col].fillna(df[col].median(), inplace=True)

categorical_cols = [
    'gender',
    'smoking_history'
]

for col in categorical_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

# FINAL CHECK

print("\nFinal Missing Values:")
print(df.isnull().sum())

print("\nFinal Shape:", df.shape)

# SAVE CLEANED DATA

OUTPUT_PATH = "../data/processed/cleaned_diabetes.csv"

df.to_csv(OUTPUT_PATH, index=False)

print(f"\nCleaned Dataset Saved At:")
print(OUTPUT_PATH)