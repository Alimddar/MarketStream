from sqlalchemy.orm import Session
from models.video_call import VideoCall
from datetime import datetime

def create_video_call(db: Session, user_id: int, start_time: datetime, end_time: datetime = None):
    db_video_call = VideoCall(user_id=user_id, start_time=start_time, end_time=end_time)
    db.add(db_video_call)
    db.commit()
    db.refresh(db_video_call)
    return db_video_call

def end_video_call(db: Session, call_id: int, end_time: datetime):
    db_video_call = db.query(VideoCall).filter(VideoCall.call_id == call_id).first()
    if db_video_call:
        db_video_call.end_time = end_time
        db.commit()
        db.refresh(db_video_call)
        return db_video_call
    return None

def get_video_call(db: Session, call_id: int):
    return db.query(VideoCall).filter(VideoCall.call_id == call_id).first()

def get_user_active_video_calls(db: Session, user_id: int, skip: int = 0):
    return db.query(VideoCall).filter(VideoCall.user_id == user_id, VideoCall.end_time == None).offset(skip).all()

def get_recent_video_calls(db: Session):
    return db.query(VideoCall).order_by(VideoCall.start_time.desc()).all()

def delete_video_call(db: Session, call_id: int):
    db_video_call = db.query(VideoCall).filter(VideoCall.call_id == call_id).first()
    if db_video_call:
        db.delete(db_video_call)
        db.commit()
        return db_video_call
    return None
