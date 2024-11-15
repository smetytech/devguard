from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from datetime import datetime
from devguard.agent.setup import graph
from devguard.agent.utils import print_stream
import json
app = FastAPI()

# CORS configuration
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Demo credentials for authentication
DEMO_CREDENTIALS = {
    "username": "user",
    "password": "password"
}

# Define a Pydantic model for input validation
class LoginRequest(BaseModel):
    username: str
    password: str

@app.post("/authenticate")
async def authenticate_user(credentials: LoginRequest):
    """
    Authenticate user with demo credentials.
    """
    if (credentials.username == DEMO_CREDENTIALS["username"] and
            credentials.password == DEMO_CREDENTIALS["password"]):
        return {"status": "success", "message": "Authenticated successfully!"}
    
    raise HTTPException(status_code=401, detail="Invalid username or password")

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            print(f"Received data from client")
            config = {"configurable": {"thread_id": "demo"}, "recursion_limit": 100}
            async for s in graph.astream( {"messages": [("user", data)]}, config, stream_mode="values"):
                for response in s["messages"]:
                    print(response)
                    if isinstance(response, tuple):
                        print(response)
                    else:
                        if data != response.content:
                            if len(response.content) < 2:
                                await websocket.send_text(json.dumps({"type": "TOOL", "name": response.tool_calls[0]["name"], "content": str(response.additional_kwargs), "timestamp": str(datetime.now().isoformat())}))
                            else:
                                await websocket.send_text(json.dumps({"type": "AGENT", "name": "DevGuard", "content": response.content, "timestamp": str(datetime.now().isoformat())}))

            
    except WebSocketDisconnect:
        print("WebSocket disconnected")


