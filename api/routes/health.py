from fastapi import APIRouter
from datetime import datetime

router = APIRouter()


@router.get("/health")

def health_check():

    return {
        "status": "healthy",
        "service": "Healthcare AI Platform",
        "timestamp": datetime.utcnow(),
        "version": "1.0.0"
    }