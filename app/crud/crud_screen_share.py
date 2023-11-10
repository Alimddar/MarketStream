from sqlalchemy.orm import Session
from models.screen_share import ScreenShare
from datetime import datetime

def start_screen_share(db: Session, session_id: int, user_id: int, start_time: datetime, share_link: str):
    db_screen_share = ScreenShare(session_id=session_id, user_id=user_id, start_time=start_time, share_link=share_link)
    db.add(db_screen_share)
    db.commit()
    db.refresh(db_screen_share)
    return db_screen_share

def end_screen_share(db: Session, share_id: int, end_time: datetime):
    db_screen_share = db.query(ScreenShare).filter(ScreenShare.share_id == share_id).first()
    if db_screen_share:
        db_screen_share.end_time = end_time
        db.commit()
        db.refresh(db_screen_share)
        return db_screen_share
    return None

def get_active_screen_shares(db: Session, user_id: int, skip: int = 0):
    return db.query(ScreenShare).filter(ScreenShare.user_id == user_id, ScreenShare.end_time == None).offset(skip).all()

def get_screen_share(db: Session, share_id: int):
    return db.query(ScreenShare).filter(ScreenShare.share_id == share_id).first()

def delete_screen_share(db: Session, share_id: int):
    db_screen_share = db.query(ScreenShare).filter(ScreenShare.share_id == share_id).first()
    if db_screen_share:
        db.delete(db_screen_share)
        db.commit()
        return db_screen_share
    return None
