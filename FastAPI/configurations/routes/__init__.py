from FastAPI.configurations.routes.routes import Routes
from FastAPI.internal.routes import health

__routes__ = Routes(routers=(health.router, ))