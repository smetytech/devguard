from fastapi import WebSocket, WebSocketDisconnect, APIRouter
from backend.ws.connection import ConnectionManager
from backend.tasks import run_trivy_scan, run_trufflehog_scan
from backend.logger import log_event

websocket_router = APIRouter()
manager = ConnectionManager()

@websocket_router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    log_event("WebSocket connection established.")

    try:
        while True:
            data = await websocket.receive_text()

            # Handle specific commands
            if data.startswith("scan:"):
                target = data.split(":")[1].strip()
                result = run_trivy_scan(target)
                await manager.send_personal_message(result, websocket)
            elif data.startswith("test:"):
                repo = data.split(":")[1].strip()
                result = run_trufflehog_scan(repo)
                await manager.send_personal_message(result, websocket)
            else:
                # Broadcast generic messages
                await manager.broadcast(f"Client says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        log_event("WebSocket connection closed.")
