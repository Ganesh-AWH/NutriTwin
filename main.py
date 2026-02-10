from fastapi import FastAPI
from api.routes import router

app = FastAPI(
    title="Nutrition AI",
    description="Personalized nutrition planning with AI",
    version="1.0.0"
)

app.include_router(router)
