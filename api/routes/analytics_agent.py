from fastapi import APIRouter

from api.schemas import ChatRequest

from agents.healthcare_analytics_agent import (
    DataAnalystAgent
)

router = APIRouter()

# DATA ANALYST AGENT ENDPOINT

@router.post("/analytics-agent")

def analytics_agent(data: ChatRequest):

    try:

        result = DataAnalystAgent(
            data.question
        )

        return {

            "success": True,

            "response": result
        }

    except Exception as e:

        return {

            "success": False,

            "error": str(e)
        }