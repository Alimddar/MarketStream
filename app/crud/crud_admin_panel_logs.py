from sqlalchemy.orm import Session
from models.admin_panel_logs import AdminPanelLogs

def log_admin_action(db: Session, admin_user_id: int, action: str):
    db_log = AdminPanelLogs(admin_user_id=admin_user_id, action=action)
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log

def get_admin_logs(db: Session, log_id: int):
    return db.query(AdminPanelLogs).filter(AdminPanelLogs.log_id == log_id).first()

def get_admin_logs_by_user(db: Session, admin_user_id: int, skip: int = 0):
    return db.query(AdminPanelLogs).filter(AdminPanelLogs.admin_user_id == admin_user_id).offset(skip).all()

def get_recent_admin_logs(db: Session):
    return db.query(AdminPanelLogs).order_by(AdminPanelLogs.log_time.desc()).all()

def update_admin_log(db: Session, log_id: int, action: str):
    db_log = db.query(AdminPanelLogs).filter(AdminPanelLogs.log_id == log_id).first()
    if db_log:
        db_log.action = action
        db.commit()
        db.refresh(db_log)
        return db_log
    return None

def delete_admin_log(db: Session, log_id: int):
    db_log = db.query(AdminPanelLogs).filter(AdminPanelLogs.log_id == log_id).first()
    if db_log:
        db.delete(db_log)
        db.commit()
        return db_log
    return None