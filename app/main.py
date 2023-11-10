from fastapi import FastAPI,Depends
from sqlalchemy import create_engine
from datetime import datetime
from models.base import Base
from sqlalchemy.orm import sessionmaker, Session

app = FastAPI()

engine = create_engine("postgresql+pg8000://root:root@localhost:5432/product_db", echo=True)
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()