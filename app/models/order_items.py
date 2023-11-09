from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class OrderItem(Base):
    __tablename__ = 'order_items'  

    order_item_id = Column(Integer, primary_key=True, index=True) 
    product_id = Column(Integer, ForeignKey('products.product_id'), index=True)  
    quantity = Column(Integer)
    price_at_time_of_order = Column(Float)
    created_at = Column(DateTime)  

    product = relationship("Product", back_populates="order_items")

