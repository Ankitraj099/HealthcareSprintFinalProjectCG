from fastapi import APIRouter

from api.database import prediction_collection
from api.schemas import PatientData

from datetime import datetime

router = APIRouter()


@router.post("/add-patient")

def add_patient(data: PatientData):

    try:

        patient_record = {

            "gender": data.gender,
            "age": data.age,
            "hypertension": data.hypertension,
            "heart_disease": data.heart_disease,
            "smoking_history": data.smoking_history,
            "bmi": data.bmi,
            "HbA1c_level": data.HbA1c_level,
            "blood_glucose_level": data.blood_glucose_level,
            "created_at": datetime.utcnow()

        }

        result = prediction_collection.insert_one(
            patient_record
        )

        return {

            "success": True,
            "message": "Patient added successfully",
            "patient_id": str(result.inserted_id)

        }

    except Exception as e:

        return {

            "success": False,
            "error": str(e)

        }