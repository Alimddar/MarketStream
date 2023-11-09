from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products' 

    product_id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, index=True)
    name = Column(String)
    description = Column(String)  
    price = Column(Float)
    in_stock = Column(Boolean) 
    stock_quantity = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())  
    updated_at = Column(DateTime(timezone=True), onupdate=func.now()) 