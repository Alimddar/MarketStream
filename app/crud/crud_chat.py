from sqlalchemy.orm import Session
from datetime import datetime
from models.chat import Chat

def create_chat_message(db: Session, sender_user_id: int, receiver_user_id: int, message: str, sent_at: datetime):
    db_chat = Chat(sender_user_id=sender_user_id, receiver_user_id=receiver_user_id, message=message, sent_at=sent_at)
    db.add(db_chat)
    db.commit()
    db.refresh(db_chat)
    return db_chat

def get_chat_message(db: Session, chat_id: int):
    return db.query(Chat).filter(Chat.chat_id == chat_id).first()

def get_user_chats(db: Session, user_id: int, skip: int = 0):
    return db.query(Chat).filter((Chat.sender_user_id == user_id) | (Chat.receiver_user_id == user_id)).offset(skip).all()

def update_chat_message(db: Session, chat_id: int, message: str):
    db_chat = db.query(Chat).filter(Chat.chat_id == chat_id).first()
    if db_chat:
        db_chat.message = message
        db.commit()
        db.refresh(db_chat)
        return db_chat
    return None

def delete_chat_message(db: Session, chat_id: int):
    db_chat = db.query(Chat).filter(Chat.chat_id == chat_id).first()
    if db_chat:
        db.delete(db_chat)
        db.commit()
        return db_chat
    return None
