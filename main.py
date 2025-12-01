from fastapi import FastAPI
from routers import api_key

app = FastAPI(
    title="Books Management System"
)

app.include_router(api_key.router, prefix='/api/validate_key')