import json
import logging
from datetime import datetime

from devguard.agent.setup import SYSTEM_PROMPT, agent_tools, model
from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent

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


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await websocket.accept()
    # Initialize the memory
    memory = MemorySaver()
    try:
        while True:
            # Receive data from the client
            data = await websocket.receive_text()
            
            # Configure the graph stream
            config = {"configurable": {"thread_id": client_id, "session_id": client_id}, "recursion_limit": 100}
            graph = create_react_agent(
                model,
                tools=agent_tools,
                state_modifier=SYSTEM_PROMPT,
                checkpointer=memory,
            )
            res = graph.astream(
                {"messages": [("user", data)]}, config, stream_mode="values"
            )
            # Process the received data through the graph
            seen_messages = set()  # To track seen messages

            async for s in graph.astream({"messages": [("user", data)]}, config, stream_mode="values"):
                for response in s["messages"]:
                    # Use a unique identifier for messages, such as their content or a unique ID if available
                    message_id = response.content  # Assuming `content` is unique

                    if message_id not in seen_messages:
                        seen_messages.add(message_id)  # Mark this message as seen

                        # Process or display the new message
                        if len(response.content) < 2:
                            # Tool response
                            await websocket.send_text(
                                json.dumps({
                                    "type": "TOOL",
                                    "name": "Tool",
                                    "content": str(response.additional_kwargs),
                                    "timestamp": str(datetime.now().isoformat()),
                                })
                            )
                        else:
                            # Agent response
                            await websocket.send_text(
                                json.dumps({
                                    "type": "AGENT",
                                    "name": "Agent",
                                    "content": response.content,
                                    "timestamp": str(datetime.now().isoformat()),
                                })
                            )
            # Clean the memory
    except WebSocketDisconnect:
        # Handle WebSocket disconnection
        memory = MemorySaver()
        print("WebSocket disconnected")
