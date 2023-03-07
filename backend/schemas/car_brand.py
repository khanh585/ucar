from pydantic import BaseModel
from typing import Optional

class CarBrandBase(BaseModel):
    name: str
    logo: Optional[str]
    

class CarBrandResponse(CarBrandBase):
    id: int
    

