from models.user import User
from sqlalchemy.orm import Session

def create_user(db: Session, username: str, password: str, name: str, surname: str, is_admin: bool = False):
    db_user = User(username=username, password=password, name=name, surname=surname, is_admin=is_admin)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.user_id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def get_users(db: Session, skip: int = 0):
    return db.query(User).offset(skip).all()

def update_user(db: Session, user_id: int, name: str, surname: str, is_admin: bool):
    db_user = db.query(User).filter(User.user_id == user_id).first()
    if db_user:
        db_user.name = name
        db_user.surname = surname
        db_user.is_admin = is_admin
        db.commit()
        db.refresh(db_user)
        return db_user
    return None

def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.user_id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return db_user
    return None