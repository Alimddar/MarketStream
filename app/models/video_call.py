from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class VideoCall(Base):
    __tablename__ = 'video_calls' 

    call_id = Column(Integer, primary_key=True, index=True)
    host_user_id = Column(Integer, ForeignKey('users.user_id'), index=True)  
    guest_user_id = Column(Integer, ForeignKey('users.user_id'))
    start_time = Column(DateTime) 
    end_time = Column(DateTime)
    call_link = Column(String)  

    host_user = relationship("User", foreign_keys=[host_user_id])
    guest_user = relationship("User", foreign_keys=[guest_user_id])
