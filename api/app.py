from fastapi import FastAPI

from api.routes.prediction import router as prediction_router
from api.routes.health import router as health_router
from api.routes.patient_history import router as history_router
from api.routes.patient_data import router as patient_router
from api.routes.rag_chat import router as rag_router
from api.routes.agent_chat import router as agent_router
from api.routes.analytics_agent import (
    router as analytics_agent_router
)

app = FastAPI(
    title="Healthcare AI Platform",
    version="1.0"
)

# INCLUDE ROUTES

app.include_router(health_router)

app.include_router(prediction_router)

app.include_router(history_router)

app.include_router(patient_router)

app.include_router(rag_router)

app.include_router(agent_router)

app.include_router(
    analytics_agent_router
)


@app.get("/")

def home():

    return {
        "message": "Healthcare AI Platform Running"
    }