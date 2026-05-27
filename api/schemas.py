from pydantic import BaseModel

# PATIENT PREDICTION SCHEMA

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


# CHATBOT SCHEMA

class ChatRequest(BaseModel):

    question: str


# SYMPTOM SCHEMA

class SymptomRequest(BaseModel):

    symptoms: str