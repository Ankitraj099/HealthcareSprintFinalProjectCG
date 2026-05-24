from rag.rag_pipeline import ask_rag


def medical_rag_agent(query):

    response = ask_rag(query)

    return {

        "agent": "Medical RAG Agent",

        "response": response
    }