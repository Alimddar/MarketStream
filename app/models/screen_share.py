from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from .base import Base
from sqlalchemy.orm import relationship

class ScreenShare(Base):
    __tablename__ = 'screen_shares'

    share_id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey('video_calls.call_id'), index=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))  
    start_time = Column(DateTime)  
    end_time = Column(DateTime)
    share_link = Column(String)  

    video_call_session = relationship("VideoCall", foreign_keys=[session_id])
    user = relationship("User", foreign_keys=[user_id])
