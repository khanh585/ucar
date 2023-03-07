from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.connection import db_connection

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5000'],
    allow_methods =['*'],
    allow_headers=['*'],
)
db_connection.check_connection()

from routers.router import api_router

app.include_router(api_router, prefix='/v1')
