from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import List
ws_router = APIRouter(
    prefix='/ws',
    tags=['WebSocket services']
)

active_connections: List[WebSocket] = []

@ws_router.websocket("/chat")
async def websocket_chat(websocket: WebSocket):

    await websocket.accept()

    active_connections.append(websocket)

    userId = websocket.query_params.get('userId')

    try:

        while True:

            message = await websocket.receive_text()

            for connection in active_connections:

                if connection != websocket:

                    await connection.send_text(f"{userId}: {message}")

    except WebSocketDisconnect:

        active_connections.remove(websocket)

    finally:

        await websocket.close()