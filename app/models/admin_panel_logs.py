from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()

class AdminPanelLogs(Base):
    __tablename__ = 'admin_panel_logs'  
    
    log_id = Column(Integer, primary_key=True, index=True)
    admin_user_id = Column(Integer, ForeignKey('admins.user_id'), index=True)  
    action = Column(String)
    log_time = Column(DateTime, default=func.now())

    admin_user = relationship("Admin", back_populates="logs")
