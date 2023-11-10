from sqlalchemy.orm import Session
from models.order import Order

def create_order(db: Session, company_id: int, user_id: int, status: str, total_amount: float):
    db_order = Order(company_id=company_id, user_id=user_id, status=status, total_amount=total_amount)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_order(db: Session, order_id: int):
    return db.query(Order).filter(Order.order_id == order_id).first()

def get_orders(db: Session, skip: int = 0):
    return db.query(Order).offset(skip).all()

def update_order(db: Session, order_id: int, status: str, total_amount: float):
    db_order = db.query(Order).filter(Order.order_id == order_id).first()
    if db_order:
        db_order.status = status
        db_order.total_amount = total_amount
        db.commit()
        db.refresh(db_order)
        return db_order
    return None

def delete_order(db: Session, order_id: int):
    db_order = db.query(Order).filter(Order.order_id == order_id).first()
    if db_order:
        db.delete(db_order)
        db.commit()
        return db_order
    return None