from datetime import datetime
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from db.models.car_brand import CarBrand
from const import ALIVE, DELETED
from schemas.car_brand import CarBrandBase

class ServiceCarBrand:
    async def get_list_brand(self, db: Session):
        result = db.query(CarBrand).filter(CarBrand.delete_flag==ALIVE).all()
        return result
    

    async def create_brand(self, db: Session, data_in: CarBrandBase):
        db_obj = CarBrand(**jsonable_encoder(data_in))
        db_obj.create_at = datetime.utcnow()
        db_obj.update_at = datetime.utcnow()
        db_obj.delete_flag = ALIVE
        db.add(db_obj)
        db.flush()
        db.refresh(db_obj)

        return db_obj
    
    
    async def update_brand(self, db: Session, brand_id: int, data_new: CarBrandBase):
        data_old = db.query(CarBrand).filter(CarBrand.id==brand_id, CarBrand.delete_flag==ALIVE).first()
        data_old.update_at = datetime.utcnow()

        dict_new = data_new.dict(exclude_unset=True)
        for field in dict_new.keys():
            if field in data_old.__dict__.keys():
                setattr(data_old, field, dict_new[field])
        db.add(data_old)
        db.flush()

        return data_old
    
    
    async def delete_brand(self, db: Session, brand_id: int):
        db_obj = (db.query(CarBrand).filter(CarBrand.id==brand_id, 
                                                    CarBrand.delete_flag==ALIVE).first())
        if not db_obj:
            return None
        db_obj.delete_at = datetime.utcnow()
        db_obj.delete_flag = DELETED
        db.add(db_obj)
        db.flush()
        
        return db_obj
    
service_car_brand = ServiceCarBrand()
