from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from .base import Base

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class AdminPanelLogs(Base):
    __tablename__ = 'admin_panel_logs'  
    
    log_id = Column(Integer, primary_key=True, index=True)
    admin_user_id = Column(Integer, ForeignKey('users.user_id'), index=True) 
    action = Column(String)
    log_time = Column(DateTime, default=func.now())

