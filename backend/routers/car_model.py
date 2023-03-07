from fastapi import Depends, APIRouter
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from db.connection import db_connection
from service.service_car_model import service_car_model
from schemas import CarModelResposne, CarModelBase, CarModelBrandResposne
from typing import List

router = APIRouter()

@router.get("/", response_model=List[CarModelBrandResposne])
async def get(
                brand_id: int = None,
                key_word: str = None,
                db: Session = Depends(db_connection.get_session)):
    db_result = await service_car_model.get_list_model(db, brand_id, key_word)
    result = []
    for item in db_result:
        temp = CarModelBrandResposne(**jsonable_encoder(item[0]))
        temp.brand_name = item[1].name
        result.append(temp)

    return result

@router.post("/", response_model=CarModelResposne)
async def create_brand(item_in: CarModelBase,
              db: Session = Depends(db_connection.get_session)):
    result = await service_car_model.create_model(db, item_in)
    result = jsonable_encoder(result)
    return result

@router.put("/{model_id}", response_model=CarModelResposne)
async def update_brand(model_id,
                       item_in: CarModelBase,
                       db: Session = Depends(db_connection.get_session)):
    result = await service_car_model.update_brand(db, model_id, item_in)
    result = jsonable_encoder(result)
    return result

@router.delete("/{model_id}", response_model=CarModelResposne)
async def delete_brand(model_id,
                       db: Session = Depends(db_connection.get_session)):
    result = await service_car_model.delete_brand(db, model_id)
    result = jsonable_encoder(result)
    return result
