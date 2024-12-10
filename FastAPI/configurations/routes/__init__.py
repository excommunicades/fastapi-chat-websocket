from FastAPI.configurations.routes.routes import Routes
from FastAPI.internal.routes import health
from FastAPI.internal.routes.chat_websocket import chat
from FastAPI.internal.routes.auth import auth

__routes__ = Routes(routers=(health.router, chat.ws_router, auth.router))
