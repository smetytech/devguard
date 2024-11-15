from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from backend.ws.endpoints import websocket_router

app = FastAPI()

@app.get("/")
async def get_home():
    with open("backend/templates/index.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(html_content)


app.include_router(websocket_router)
