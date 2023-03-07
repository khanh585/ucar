from datetime import datetime
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from db.models.car_model import CarModel
from db.models.car_brand import CarBrand
from const import ALIVE, DELETED
from schemas.car_model import CarModelBase


class ServiceCarModel:
    async def get_list_model(self, db: Session, brand_id: int = None, key_word: str = None):
        db_obj = db.query(CarModel, CarBrand).join(CarBrand, CarBrand.id == CarModel.car_brand_id)

        if brand_id is not None:
            db_obj = db_obj.filter(CarModel.car_brand_id==brand_id)
        if key_word is not None:
            db_obj = db_obj.filter(CarModel.name.like(f'%{key_word}%'))
        result = db_obj.all()
        return result
    

    async def create_model(self, db: Session, data_in: CarModelBase):
        db_obj = CarModel(**jsonable_encoder(data_in))
        db_obj.create_at = datetime.utcnow()
        db_obj.update_at = datetime.utcnow()
        db_obj.delete_flag = ALIVE
        db.add(db_obj)
        db.flush()
        db.refresh(db_obj)

        return db_obj
    
    
    async def update_brand(self, db: Session, model_id, data_new: CarModelBase):
        data_old = db.query(CarModel).filter(CarModel.id==model_id, CarModel.delete_flag==ALIVE).first()
        data_old.update_at = datetime.utcnow()

        dict_new = data_new.dict(exclude_unset=True)
        for field in dict_new.keys():
            if field in data_old.__dict__.keys():
                setattr(data_old, field, dict_new[field])
        db.add(data_old)
        db.flush()

        return data_old
    
    
    async def delete_brand(self, db: Session, model_id: int):
        db_obj = (db.query(CarModel)
                            .filter(CarModel.id==model_id, 
                                    CarModel.delete_flag==ALIVE)
                            .first())
        if not db_obj:
            return None
        db_obj.delete_at = datetime.utcnow()
        db_obj.delete_flag = DELETED
        db.add(db_obj)
        db.flush()
        
        return db_obj
    
service_car_model = ServiceCarModel()
    