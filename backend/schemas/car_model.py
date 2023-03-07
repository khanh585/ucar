from pydantic import BaseModel
from typing import Optional

class CarModelBase(BaseModel):
    car_brand_id: int
    name: str
    model_general: str
    model_brand: str
    image: Optional[str]

class CarModelResposne(CarModelBase):
    id: int

class CarModelBrandResposne(CarModelResposne):
    brand_name: Optional[str]
