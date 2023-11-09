from fastapi import FastAPI
from sqlmodel import SQLModel, create_engine

app = FastAPI()

DATABASE_URL = "postgresql+pg8000://root:root@localhost:5432/product_db"

engine = create_engine(DATABASE_URL)
SQLModel.metadata.create_all(engine)

