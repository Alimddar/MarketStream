from sqlalchemy.orm import Session
from datetime import datetime
from models.order_items import OrderItem

def create_order_item(db: Session, product_id: int, quantity: int, price_at_time_of_order: float, created_at: datetime):
    db_order_item = OrderItem(product_id=product_id, quantity=quantity, price_at_time_of_order=price_at_time_of_order, created_at=created_at)
    db.add(db_order_item)
    db.commit()
    db.refresh(db_order_item)
    return db_order_item

def get_order_item(db: Session, order_item_id: int):
    return db.query(OrderItem).filter(OrderItem.order_item_id == order_item_id).first()

def get_order_items_by_product(db: Session, product_id: int, skip: int = 0):
    return db.query(OrderItem).filter(OrderItem.product_id == product_id).offset(skip).all()

def update_order_item(db: Session, order_item_id: int, quantity: int, price_at_time_of_order: float):
    db_order_item = db.query(OrderItem).filter(OrderItem.order_item_id == order_item_id).first()
    if db_order_item:
        db_order_item.quantity = quantity
        db_order_item.price_at_time_of_order = price_at_time_of_order
        db.commit()
        db.refresh(db_order_item)
        return db_order_item
    return None

def delete_order_item(db: Session, order_item_id: int):
    db_order_item = db.query(OrderItem).filter(OrderItem.order_item_id == order_item_id).first()
    if db_order_item:
        db.delete(db_order_item)
        db.commit()
        return db_order_item
    return None
