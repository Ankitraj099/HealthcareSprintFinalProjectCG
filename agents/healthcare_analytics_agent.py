import pandas as pd

from pathlib import Path

# -----------------------------------
# LOAD DATASET
# -----------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = (
    BASE_DIR
    / "src"
    / "data"
    / "processed"
    / "final_diabetes.csv"
)

df = pd.read_csv(DATA_PATH)

# -----------------------------------
# DATA ANALYST AGENT
# -----------------------------------

def DataAnalystAgent(query):

    query = query.lower()

    # -----------------------------------
    # TOTAL PATIENTS
    # -----------------------------------

    if "total patients" in query:

        return {

            "agent": "DataAnalystAgent",

            "response": f"""
            Total patients in dataset:
            {len(df)}
            """
        }

    # -----------------------------------
    # DIABETIC PATIENTS
    # -----------------------------------

    elif "diabetic" in query:

        diabetic_patients = int(
            df["diabetes"].sum()
        )

        percentage = round(
            (
                diabetic_patients / len(df)
            ) * 100,
            2
        )

        return {

            "agent": "DataAnalystAgent",

            "response": f"""
            Diabetic Patients:
            {diabetic_patients}

            Percentage:
            {percentage}%
            """
        }

    # -----------------------------------
    # AVERAGE GLUCOSE
    # -----------------------------------

    elif "glucose" in query:

        avg_glucose = round(
            df["blood_glucose_level"].mean(),
            2
        )

        return {

            "agent": "DataAnalystAgent",

            "response": f"""
            Average Blood Glucose Level:
            {avg_glucose}
            """
        }

    # -----------------------------------
    # AVERAGE BMI
    # -----------------------------------

    elif "bmi" in query:

        avg_bmi = round(
            df["bmi"].mean(),
            2
        )

        return {

            "agent": "DataAnalystAgent",

            "response": f"""
            Average BMI:
            {avg_bmi}
            """
        }

    # -----------------------------------
    # HYPERTENSION ANALYSIS
    # -----------------------------------

    elif "hypertension" in query:

        hypertension_patients = int(
            df["hypertension"].sum()
        )

        return {

            "agent": "DataAnalystAgent",

            "response": f"""
            Patients with Hypertension:
            {hypertension_patients}
            """
        }

    # -----------------------------------
    # HEART DISEASE ANALYSIS
    # -----------------------------------

    elif "heart disease" in query:

        heart_patients = int(
            df["heart_disease"].sum()
        )

        return {

            "agent": "DataAnalystAgent",

            "response": f"""
            Patients with Heart Disease:
            {heart_patients}
            """
        }

    # -----------------------------------
    # DEFAULT ANALYTICS SUMMARY
    # -----------------------------------

    else:

        return {

            "agent": "DataAnalystAgent",

            "response": f"""
            Healthcare Dataset Summary:

            Total Patients:
            {len(df)}

            Diabetic Patients:
            {int(df["diabetes"].sum())}

            Average Glucose Level:
            {round(df["blood_glucose_level"].mean(), 2)}

            Average BMI:
            {round(df["bmi"].mean(), 2)}
            """
        }