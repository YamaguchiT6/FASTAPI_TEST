from fastapi import FastAPI

from routers import task
from middleware.middleware import ErrorHandlingMiddleware

app = FastAPI()
app.add_middleware(ErrorHandlingMiddleware)
app.include_router(task.router)