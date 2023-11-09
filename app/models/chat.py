from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()

class Chat(Base):
    __tablename__ = 'chats'

    chat_id = Column(Integer, primary_key=True, index=True)
    sender_user_id = Column(Integer, ForeignKey('users.user_id'), index=True) 
    receiver_user_id = Column(Integer, ForeignKey('users.user_id'))  
    message = Column(String)  
    sent_at = Column(DateTime, default=func.now())  

    sender = relationship("User", foreign_keys=[sender_user_id])
    receiver = relationship("User", foreign_keys=[receiver_user_id])
