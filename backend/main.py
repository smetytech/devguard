from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

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
            await websocket.send_text(data)
    except WebSocketDisconnect:
        print("WebSocket disconnected")


