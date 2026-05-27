from openai import AzureOpenAI
from dotenv import load_dotenv

from rag.retriever import retriever

import os


load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")

# RAG FUNCTION

def ask_rag(question):

    # Retrieve relevant docs
    docs = retriever.invoke(question)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
    Answer the healthcare question using
    the provided medical context.

    Context:
    {context}

    Question:
    {question}

    Give medically accurate and safe answers.
    """

    response = client.chat.completions.create(

        model=deployment_name,

        messages=[

            {
                "role": "system",
                "content": "You are an enterprise healthcare AI assistant."
            },

            {
                "role": "user",
                "content": prompt
            }

        ],

        temperature=0.3,
        max_tokens=500

    )

    answer = response.choices[0].message.content

    return answer