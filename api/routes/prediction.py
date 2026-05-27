from fastapi import APIRouter
from pydantic import BaseModel
import joblib
import pandas as pd

from utils.azure_blob import upload_prediction_to_blob

router = APIRouter()

# Load model and encoders
model = joblib.load("src/models/diabetes_model.pkl")

gender_encoder = joblib.load(
    "src/models/gender_encoder.pkl"
)

smoking_encoder = joblib.load(
    "src/models/smoking_encoder.pkl"
)

scaler = joblib.load("src/models/scaler.pkl")


class PatientData(BaseModel):

    name: str

    gender: str
    age: int

    hypertension: str
    heart_disease: str

    smoking_history: str

    bmi: float
    HbA1c_level: float
    blood_glucose_level: int


@router.post("/predict")
def predict(data: PatientData):

    # Encode gender
    gender_encoded = gender_encoder.transform(
        [data.gender]
    )[0]

    # Encode smoking history
    smoking_encoded = smoking_encoder.transform(
        [data.smoking_history]
    )[0]

    # Convert hypertension
    hypertension_encoded = (
        1 if data.hypertension.lower() == "yes"
        else 0
    )

    # Convert heart disease
    heart_disease_encoded = (
        1 if data.heart_disease.lower() == "yes"
        else 0
    )

    # Create dataframe
    input_df = pd.DataFrame([{
        "gender": gender_encoded,
        "age": data.age,
        "hypertension": hypertension_encoded,
        "heart_disease": heart_disease_encoded,
        "smoking_history": smoking_encoded,
        "bmi": data.bmi,
        "HbA1c_level": data.HbA1c_level,
        "blood_glucose_level": data.blood_glucose_level
    }])

    # Scale input
    scaled_input = scaler.transform(input_df)

    # Prediction
    prediction = model.predict(
        scaled_input
    )[0]

    probability = model.predict_proba(
        scaled_input
    )[0][1]

    # Upload prediction to blob
    upload_prediction_to_blob({
        "gender": data.gender,
        "age": data.age,
        "prediction": int(prediction),
        "confidence": float(probability)
    })

    return {
        "patient_name": data.name,
        "prediction": int(prediction),
        "confidence": round(
            float(probability) * 100,
            2
        ),
        "status": (
            "Diabetic"
            if prediction == 1
            else "Non-Diabetic"
        )
    }