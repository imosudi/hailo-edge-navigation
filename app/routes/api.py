from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health_check():
    return {
        "status": "ok",
        "service": "edge-ai-navigation"
    }


@router.get("/metrics")
async def metrics():
    return {
        "fps": 0,
        "cpu_usage": 0,
        "memory_usage": 0,
        "hailo_status": "not_connected"
    }