from fastapi import WebSocket, WebSocketDisconnect, APIRouter
from backend.ws.connection import ConnectionManager
from backend.auth import validate_token
from backend.tasks import run_trivy_scan, run_trufflehog_scan
from backend.logger import log_event

websocket_router = APIRouter()
manager = ConnectionManager()

@websocket_router.websocket("/ws/{token}")
async def websocket_endpoint(websocket: WebSocket, token: str):
    # Validate token
    if not validate_token(token):
        await websocket.close(code=1008)
        return
    await manager.connect(websocket)
    log_event(f"WebSocket connection established with token: {token}")

    try:
        while True:
            data = await websocket.receive_text()
            if data.startswith("scan:"):
                target = data.split(":")[1]
                result = run_trivy_scan(target)
                await manager.send_personal_message(result, websocket)
            elif data.startswith("test:"):
                repo = data.split(":")[1]
                result = run_trufflehog_scan(repo)
                await manager.send_personal_message(result, websocket)
            else:
                await manager.broadcast(f"Message: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        log_event(f"WebSocket connection closed for token: {token}")
        await manager.broadcast("A user disconnected.")
