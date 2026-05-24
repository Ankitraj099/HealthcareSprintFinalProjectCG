from fastapi import APIRouter

from api.schemas import ChatRequest

from agents.ai_orchestrator_agent import (
    run_healthcare_agents
)

router = APIRouter()


@router.post("/agent-chat")

def agent_chat(data: ChatRequest):

    try:

        result = run_healthcare_agents(
            data.question
        )

        return {

            "success": True,

            "agents_used": len(result),

            "responses": result
        }

    except Exception as e:

        return {

            "success": False,

            "error": str(e)
        }