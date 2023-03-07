from fastapi import APIRouter
from . import car_brand, car_model

api_router = APIRouter()
api_router.include_router(car_brand.router, prefix="/brand", tags=["brand"])
api_router.include_router(car_model.router, prefix="/model", tags=["model"])