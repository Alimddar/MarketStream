from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .base import Base

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True) 
    password = Column(String)
    name = Column(String)
    surname = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())  
    last_login = Column(DateTime(timezone=True))  
    is_admin = Column(Boolean, default=False)

    orders = relationship("Order", back_populates="user")
