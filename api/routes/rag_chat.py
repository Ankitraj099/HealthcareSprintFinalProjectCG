from fastapi import APIRouter

from api.schemas import ChatRequest

from rag.rag_pipeline import ask_rag

router = APIRouter()


@router.post("/Document Assistant Agent")

def medical_rag_chat(data: ChatRequest):

    try:

        answer = ask_rag(data.question)

        return {

            "success": True,
            "question": data.question,
            "response": answer

        }

    except Exception as e:

        return {

            "success": False,
            "error": str(e)

        }