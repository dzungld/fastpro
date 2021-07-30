import uvicorn

from fastapi import FastAPI

from app.api.v1 import api_router

app = FastAPI(title="FastPro - Project Management System")

app.include_router(api_router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
