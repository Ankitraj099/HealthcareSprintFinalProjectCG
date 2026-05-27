from agents.medical_rag_agent import medical_rag_agent

from agents.symptom_triage_agent import (
    symptom_triage_agent
)

from agents.healthcare_analytics_agent import (
    DataAnalystAgent
)


def run_healthcare_agents(query):

    responses = []

    # RAG AGENT

    rag_response = medical_rag_agent(query)

    responses.append(rag_response)

    # SYMPTOM AGENT

    symptom_response = symptom_triage_agent(
        query
    )

    responses.append(symptom_response)

    # ANALYTICS AGENT

    if (
        "analytics" in query.lower()
        or
        "statistics" in query.lower()
        or
        "diabetes" in query.lower()
    ):

        analytics_response = (
        DataAnalystAgent(query)
        )

        responses.append(
            analytics_response
        )

    return responses