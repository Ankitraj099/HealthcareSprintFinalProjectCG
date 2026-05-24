from fastapi import APIRouter

from api.database import prediction_collection

router = APIRouter()


@router.get("/patient-history")
def get_patient_history():

    try:

        patients = list(
            prediction_collection.find({})
        )

        # Convert ObjectId to string
        for patient in patients:

            patient["_id"] = str(patient["_id"])

        return {

            "success": True,
            "total_records": len(patients),
            "patients": patients

        }

    except Exception as e:

        return {

            "success": False,
            "error": str(e)

        }