from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Company(Base):
    __tablename__ = 'companies'

    company_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String)  
    contact_email = Column(String)  
    created_at = Column(DateTime, default=func.now())  

