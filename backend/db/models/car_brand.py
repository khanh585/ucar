
from sqlalchemy import Column, DateTime, Integer, String, Boolean
from db.base import Base


class CarBrand(Base):
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    logo = Column(String(255))
    create_at = Column(DateTime)
    update_at = Column(DateTime)
    delete_at = Column(DateTime)
    delete_flag = Column(Boolean, default=False)
