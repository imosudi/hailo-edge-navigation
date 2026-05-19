from fastapi import APIRouter, WebSocket
from dashboard.websocket_manager import ConnectionManager

router = APIRouter()
manager = ConnectionManager()


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await manager.connect(websocket)

    while True:
        await websocket.receive_text()