from sqlalchemy import Column, Integer, String, DateTime
from .base import Base
from sqlalchemy.orm import relationship

from sqlalchemy.sql import func


class Company(Base):
    __tablename__ = 'companies'

    company_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String)  
    contact_email = Column(String)  
    created_at = Column(DateTime, default=func.now())  

    orders = relationship("Order", back_populates="company")

