def symptom_triage_agent(query):

    symptoms = {

        "fever": "may indicate an infection or viral illness.",
        "cough": "can be associated with respiratory infections, allergies, or flu.",
        "headache": "may occur due to stress, dehydration, migraine, or infections.",
        "pain": "could be related to injury, inflammation, or internal medical conditions.",
        "cold": "may indicate a common viral infection.",
        "fatigue": "can be a symptom of diabetes, anemia, stress, or lack of sleep.",
        "vomiting": "may be caused by food poisoning, infection, or digestive disorders.",
        "nausea": "can occur due to stomach infections, acidity, or other illnesses.",
        "dizziness": "may be linked to low blood pressure, dehydration, or weakness.",
        "weakness": "can result from nutritional deficiency, illness, or fatigue.",
        "high blood pressure": "may increase the risk of heart disease and stroke.",
        "hypertension": "is a serious condition related to elevated blood pressure.",
        "chest pain": "may indicate heart-related problems and requires medical attention.",
        "diabetes": "is a metabolic disorder associated with high blood sugar levels.",
        "blurred vision": "can be associated with diabetes, eye strain, or vision disorders.",
        "shortness of breath": "may indicate respiratory or cardiovascular issues."
    }

    matched = []

    for symptom, explanation in symptoms.items():

        if symptom in query.lower():

            matched.append(
                f"• {symptom.title()} → {explanation}"
            )

    if matched:

        return {

            "agent": "Symptom Triage Agent",

            "response": f"""
Detected Symptoms:

{chr(10).join(matched)}

Initial Health Assessment:
The detected symptoms may indicate a mild to moderate medical condition.
Some symptoms could also be associated with chronic illnesses such as diabetes,
hypertension, respiratory infections, or general weakness.

Recommendation:
It is strongly advised to monitor your symptoms carefully and consult a healthcare
professional for accurate diagnosis and treatment.

Emergency Advice:
If symptoms become severe, such as chest pain, breathing difficulty,
extreme weakness, or persistent vomiting, seek immediate medical attention.
"""
        }

    return {

        "agent": "Symptom Triage Agent",

        "response": """
No major symptoms were detected from the provided query.

Recommendation:
Maintain a healthy lifestyle, stay hydrated, eat nutritious food,
exercise regularly, and consult a healthcare professional if you
experience any unusual symptoms in the future.
"""
    }