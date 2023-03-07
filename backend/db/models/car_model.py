
from sqlalchemy import Column, DateTime, Integer, String, Boolean, ForeignKey
from db.base import Base

class CarModel(Base):
    __table_args__ = {"schema": "ucar-01"}
    __tablename__ = 'car_model'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    car_brand_id = Column(Integer, ForeignKey('ucar-01.car_brand.id'), nullable=False)
    name = Column(String(200))
    model_general = Column(String(15))
    model_brand = Column(String(50))
    image = Column(String(255))
    create_at = Column(DateTime)
    update_at = Column(DateTime)
    delete_at = Column(DateTime)
    delete_flag = Column(Boolean, default=False)
