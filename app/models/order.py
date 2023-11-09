from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey('companies.company_id'), index=True) 
    user_id = Column(Integer, ForeignKey('users.user_id'))  
    status = Column(String)  
    total_amount = Column(Float)  
    created_at = Column(DateTime(timezone=True), server_default=func.now()) 
    updated_at = Column(DateTime(timezone=True), onupdate=func.now()) 

    company = relationship("Company", back_populates="orders")
    user = relationship("User", back_populates="orders")