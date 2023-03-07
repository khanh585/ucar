from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.models.car_brand import CarBrand
from db.models.car_model import CarModel 
from db.connection import db_connection

db_connection.check_connection()
db_connection.create_table_model()


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5000'],
    allow_methods =['*'],
    allow_headers=['*'],
)


from routers.router import api_router

app.include_router(api_router, prefix='/v1')
