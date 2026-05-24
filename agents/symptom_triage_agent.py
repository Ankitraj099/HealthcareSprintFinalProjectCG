def symptom_triage_agent(query):

    symptoms = [

    "fever",
    "cough",
    "headache",
    "pain",
    "cold",
    "fatigue",
    "vomiting",
    "nausea",
    "dizziness",
    "weakness",
    "high blood pressure",
    "hypertension",
    "chest pain",
    "diabetes",
    "blurred vision",
    "shortness of breath"]

    matched = []

    for symptom in symptoms:

        if symptom in query.lower():

            matched.append(symptom)

    if matched:

        return {

            "agent": "Symptom Triage Agent",

            "response": f"""
            Detected symptoms:
            {', '.join(matched)}

            Possible mild infection or illness.

            Please consult a doctor
            for proper diagnosis.
            """
        }

    return {

        "agent": "Symptom Triage Agent",

        "response": "No major symptoms detected."
    }