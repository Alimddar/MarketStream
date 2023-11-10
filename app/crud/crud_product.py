from sqlalchemy.orm import Session
from models.product import Product

def create_product(db: Session, company_id: int, name: str, description: str, price: float, in_stock: bool, stock_quantity: int):
    db_product = Product(company_id=company_id, name=name, description=description, price=price, in_stock=in_stock, stock_quantity=stock_quantity)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.product_id == product_id).first()

def get_products_by_company(db: Session, company_id: int, skip: int = 0):
    return db.query(Product).filter(Product.company_id == company_id).offset(skip).all()

def get_all_products(db: Session, skip: int = 0):
    return db.query(Product).offset(skip).all()

def update_product(db: Session, product_id: int, name: str, description: str, price: float, in_stock: bool, stock_quantity: int):
    db_product = db.query(Product).filter(Product.product_id == product_id).first()
    if db_product:
        db_product.name = name
        db_product.description = description
        db_product.price = price
        db_product.in_stock = in_stock
        db_product.stock_quantity = stock_quantity
        db.commit()
        db.refresh(db_product)
        return db_product
    return None

def mark_product_out_of_stock(db: Session, product_id: int):
    db_product = db.query(Product).filter(Product.product_id == product_id).first()
    if db_product:
        db_product.in_stock = False
        db.commit()
        db.refresh(db_product)
        return db_product
    return None

def delete_product(db: Session, product_id: int):
    db_product = db.query(Product).filter(Product.product_id == product_id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return db_product
    return None