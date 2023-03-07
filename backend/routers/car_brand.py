from fastapi import Depends, APIRouter
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from db.connection import db_connection
from service.service_car_brand import service_car_brand
from schemas import CarBrandBase, CarBrandResponse
from typing import List

router = APIRouter()

@router.get("/", response_model=List[CarBrandResponse])
async def get(db: Session = Depends(db_connection.get_session)):
    result = await service_car_brand.get_list_brand(db)
    result = jsonable_encoder(result)
    return result


@router.post("/", response_model=CarBrandResponse)
async def create_brand(item_in: CarBrandBase,
              db: Session = Depends(db_connection.get_session)):
    result = await service_car_brand.create_brand(db, item_in)
    result = jsonable_encoder(result)
    return result


@router.put("/{brand_id}", response_model=CarBrandResponse)
async def update_brand(brand_id,
                       item_in: CarBrandBase,
                       db: Session = Depends(db_connection.get_session)):
    result = await service_car_brand.update_brand(db, brand_id, item_in)
    result = jsonable_encoder(result)
    return result

@router.delete("/{brand_id}", response_model=CarBrandResponse)
async def delete_brand(brand_id,
                       db: Session = Depends(db_connection.get_session)):
    result = await service_car_brand.delete_brand(db,brand_id)
    result = jsonable_encoder(result)
    return result
