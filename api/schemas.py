from pydantic import BaseModel

# -----------------------------------
# PATIENT PREDICTION SCHEMA
# -----------------------------------

class PatientData(BaseModel):

    gender: int
    age: float
    hypertension: int
    heart_disease: int
    smoking_history: int
    bmi: float
    HbA1c_level: float
    blood_glucose_level: float


# -----------------------------------
# CHATBOT SCHEMA
# -----------------------------------

class ChatRequest(BaseModel):

    question: str


# -----------------------------------
# SYMPTOM SCHEMA
# -----------------------------------

class SymptomRequest(BaseModel):

    symptoms: str