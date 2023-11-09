from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class ScreenShare(Base):
    __tablename__ = 'screen_shares' 

    share_id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey('video_call.call_id'), index=True)  
    user_id = Column(Integer, ForeignKey('users.user_id'))  
    start_time = Column(DateTime)  
    end_time = Column(DateTime)
    share_link = Column(String)  

    video_call_session = relationship("VideoCall", foreign_keys=[session_id])
    user = relationship("User", foreign_keys=[user_id])