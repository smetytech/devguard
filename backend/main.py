import json
import logging
from datetime import datetime

from devguard.agent.setup import graph
from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Initialize FastAPI application
app = FastAPI()

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# CORS configuration
origins = ["*"]

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Demo credentials for authentication
DEMO_CREDENTIALS = {"username": "user", "password": "password"}


# Pydantic model for input validation of login requests
class LoginRequest(BaseModel):
    username: str
    password: str


@app.post("/authenticate")
async def authenticate_user(credentials: LoginRequest):
    """
    Authenticate user with demo credentials.
    """
    # Check if provided credentials match the demo credentials
    if (
        credentials.username == DEMO_CREDENTIALS["username"]
        and credentials.password == DEMO_CREDENTIALS["password"]
    ):
        return {"status": "success", "message": "Authenticated successfully!"}

    # Raise exception if credentials are invalid
    raise HTTPException(status_code=401, detail="Invalid username or password")


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # Receive data from the client
            data = await websocket.receive_text()

            # Configure the graph stream
            config = {"configurable": {"thread_id": "demo"}, "recursion_limit": 100}

            # Process the received data through the graph
            async for s in graph.astream(
                {"messages": [("user", data)]}, config, stream_mode="values"
            ):
                for response in s["messages"]:
                    print(response)
                    if isinstance(response, tuple):
                        print(response)
                    else:
                        if data != response.content:
                            if len(response.content) < 2:
                                # Send tool response
                                await websocket.send_text(
                                    json.dumps(
                                        {
                                            "type": "TOOL",
                                            "name": "Tool",
                                            "content": str(response.additional_kwargs),
                                            "timestamp": str(
                                                datetime.now().isoformat()
                                            ),
                                        }
                                    )
                                )
                            else:
                                # Send agent response
                                await websocket.send_text(
                                    json.dumps(
                                        {
                                            "type": "AGENT",
                                            "name": "Agent",
                                            "content": response.content,
                                            "timestamp": str(
                                                datetime.now().isoformat()
                                            ),
                                        }
                                    )
                                )

    except WebSocketDisconnect:
        # Handle WebSocket disconnection
        print("WebSocket disconnected")
