from fastapi import FastAPI,Depends,HTTPException
from typing import List,Optional
from datetime import datetime
from sqlalchemy import create_engine
from models.base import Base
from pydantic import BaseModel
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine
from models.user import User
from models.chat import Chat
from models.admin_panel_logs import AdminPanelLogs
from models.screen_share import ScreenShare
from models.video_call import VideoCall
from models.companies import Company
from models.order_items import OrderItem
from models.product import Product
from models.order import Order
import hashlib

app = FastAPI()

engine = create_engine("postgresql+pg8000://root:root@localhost:5432/product_db", echo=True)
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class UserCreate(BaseModel):
    username: str
    password: str
    name: str
    surname: str
    is_admin: Optional[bool] = False

class VideoCallCreate(BaseModel):
    host_user_id: int
    guest_user_id: int
    start_time: datetime
    end_time: Optional[datetime] = None
    call_link: str

class ScreenShareCreate(BaseModel):
    session_id: int
    user_id: int
    start_time: datetime
    end_time: Optional[datetime] = None
    share_link: str

class ProductCreate(BaseModel):
    company_id: int
    name: str
    description: str
    price: float
    in_stock: bool
    stock_quantity: int

class OrderCreate(BaseModel):
    company_id: int
    user_id: int
    status: str
    total_amount: float

class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int
    price_at_time_of_order: float

class CompanyCreate(BaseModel):
    name: str
    address: str
    contact_email: str

class ChatCreate(BaseModel):
    sender_user_id: int
    receiver_user_id: int
    message: str

class UserUpdate(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
    name: Optional[str] = None
    surname: Optional[str] = None
    is_admin: Optional[bool] = None

class VideoCallUpdate(BaseModel):
    host_user_id: Optional[int] = None
    guest_user_id: Optional[int] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    call_link: Optional[str] = None

class ScreenShareUpdate(BaseModel):
    session_id: Optional[int] = None
    user_id: Optional[int] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    share_link: Optional[str] = None

class ProductUpdate(BaseModel):
    company_id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    in_stock: Optional[bool] = None
    stock_quantity: Optional[int] = None

class OrderUpdate(BaseModel):
    company_id: Optional[int] = None
    user_id: Optional[int] = None
    status: Optional[str] = None
    total_amount: Optional[float] = None

class OrderItemUpdate(BaseModel):
    product_id: Optional[int] = None
    quantity: Optional[int] = None
    price_at_time_of_order: Optional[float] = None

class CompanyUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    contact_email: Optional[str] = None

class ChatUpdate(BaseModel):
    message: Optional[str] = None

@app.post("/users/", tags=["user"])
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = hashlib.sha256(user.password.encode('utf-8')).hexdigest()

    db_user = User(username=user.username, name=user.name, surname=user.surname, password=hashed_password, is_admin=user.is_admin)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/", tags=["user"])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(User).offset(skip).limit(limit).all()
    return users

@app.get("/users/{user_id}", tags=["user"])
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.user_id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.put("/users/{user_id}", tags=["user"])
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.user_id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    update_data = user.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_user, key, value)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.delete("/users/{user_id}", tags=["user"])
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.user_id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(db_user)
    db.commit()
    return True

@app.post("/video_calls/", tags=['videocall'])
def create_video_call(call: VideoCallCreate, db: Session = Depends(get_db)):
    db_call = VideoCall(**call.dict())
    db.add(db_call)
    db.commit()
    db.refresh(db_call)
    return db_call

@app.get("/video_calls/{call_id}", tags=['videocall'])
def read_video_call(call_id: int, db: Session = Depends(get_db)):
    db_call = db.query(VideoCall).filter(VideoCall.call_id == call_id).first()
    if db_call is None:
        raise HTTPException(status_code=404, detail="VideoCall not found")
    return db_call

@app.put("/video_calls/{call_id}", tags=['videocall'])
def update_video_call(call_id: int, call: VideoCallUpdate, db: Session = Depends(get_db)):
    db_call = db.query(VideoCall).filter(VideoCall.call_id == call_id).first()
    if db_call is None:
        raise HTTPException(status_code=404, detail="VideoCall not found")

    update_data = call.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_call, key, value)

    db.commit()
    return db_call

@app.delete("/video_calls/{call_id}", tags=['videocall'])
def delete_video_call(call_id: int, db: Session = Depends(get_db)):
    db_call = db.query(VideoCall).filter(VideoCall.call_id == call_id).first()
    if db_call is None:
        raise HTTPException(status_code=404, detail="VideoCall not found")

    db.delete(db_call)
    db.commit()
    return True

@app.post("/screen_shares/", tags=["screenshare"])
def create_screen_share(share: ScreenShareCreate, db: Session = Depends(get_db)):
    db_share = ScreenShare(**share.dict())
    db.add(db_share)
    db.commit()
    db.refresh(db_share)
    return db_share

@app.get("/screen_shares/{share_id}", tags=["screenshare"])
def read_screen_share(share_id: int, db: Session = Depends(get_db)):
    share = db.query(ScreenShare).filter(ScreenShare.share_id == share_id).first()
    if share is None:
        raise HTTPException(status_code=404, detail="ScreenShare not found")
    return share

@app.put("/screen_shares/{share_id}", tags=["screenshare"])
def update_screen_share(share_id: int, share: ScreenShareUpdate, db: Session = Depends(get_db)):
    db_share = db.query(ScreenShare).filter(ScreenShare.share_id == share_id).first()
    if db_share is None:
        raise HTTPException(status_code=404, detail="ScreenShare not found")

    update_data = share.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_share, key, value)

    db.commit()
    return db_share

@app.delete("/screen_shares/{share_id}", tags=["screenshare"])
def delete_screen_share(share_id: int, db: Session = Depends(get_db)):
    db_share = db.query(ScreenShare).filter(ScreenShare.share_id == share_id).first()
    if db_share is None:
        raise HTTPException(status_code=404, detail="ScreenShare not found")

    db.delete(db_share)
    db.commit()
    return True

@app.post("/products/", tags=["product"])
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@app.get("/products/{product_id}", tags=["product"])
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.product_id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.put("/products/{product_id}", tags=["product"])
def update_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.product_id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    update_data = product.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_product, key, value)

    db.commit()
    return db_product

@app.delete("/products/{product_id}", tags=["product"])
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.product_id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(db_product)
    db.commit()
    return True

@app.post("/orders/", tags=["order"])
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    db_order = Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


@app.get("/orders/{order_id}", tags=["order"])
def read_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.order_id == order_id).first()
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@app.put("/orders/{order_id}", tags=["order"])
def update_order(order_id: int, order: OrderUpdate, db: Session = Depends(get_db)):
    db_order = db.query(Order).filter(Order.order_id == order_id).first()
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")

    update_data = order.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_order, key, value)

    db.commit()
    return db_order

@app.delete("/orders/{order_id}", tags=["order"])
def delete_order(order_id: int, db: Session = Depends(get_db)):
    db_order = db.query(Order).filter(Order.order_id == order_id).first()
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")

    db.delete(db_order)
    db.commit()
    return True

@app.post("/order_items/", tags=["orderitems"])
def create_order_item(order_item: OrderItemCreate, db: Session = Depends(get_db)):
    db_order_item = OrderItem(**order_item.dict())
    db.add(db_order_item)
    db.commit()
    db.refresh(db_order_item)
    return db_order_item

@app.get("/order_items/{order_item_id}", tags=["orderitems"])
def read_order_item(order_item_id: int, db: Session = Depends(get_db)):
    order_item = db.query(OrderItem).filter(OrderItem.order_item_id == order_item_id).first()
    if order_item is None:
        raise HTTPException(status_code=404, detail="OrderItem not found")
    return order_item

@app.put("/order_items/{order_item_id}", tags=["orderitems"])
def update_order_item(order_item_id: int, order_item: OrderItemUpdate, db: Session = Depends(get_db)):
    db_order_item = db.query(OrderItem).filter(OrderItem.order_item_id == order_item_id).first()
    if db_order_item is None:
        raise HTTPException(status_code=404, detail="OrderItem not found")

    update_data = order_item.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_order_item, key, value)

    db.commit()
    return db_order_item

@app.delete("/order_items/{order_item_id}", tags=["orderitems"])
def delete_order_item(order_item_id: int, db: Session = Depends(get_db)):
    db_order_item = db.query(OrderItem).filter(OrderItem.order_item_id == order_item_id).first()
    if db_order_item is None:
        raise HTTPException(status_code=404, detail="OrderItem not found")

    db.delete(db_order_item)
    db.commit()
    return True

@app.post("/companies/", tags=["company"])
def create_company(company: CompanyCreate, db: Session = Depends(get_db)):
    db_company = Company(**company.dict())
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company

@app.get("/companies/{company_id}", tags=["company"])
def read_company(company_id: int, db: Session = Depends(get_db)):
    company = db.query(Company).filter(Company.company_id == company_id).first()
    if company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return company

@app.put("/companies/{company_id}", tags=["company"])
def update_company(company_id: int, company: CompanyUpdate, db: Session = Depends(get_db)):
    db_company = db.query(Company).filter(Company.company_id == company_id).first()
    if db_company is None:
        raise HTTPException(status_code=404, detail="Company not found")

    update_data = company.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_company, key, value)

    db.commit()
    return db_company

@app.delete("/companies/{company_id}", tags=["company"])
def delete_company(company_id: int, db: Session = Depends(get_db)):
    db_company = db.query(Company).filter(Company.company_id == company_id).first()
    if db_company is None:
        raise HTTPException(status_code=404, detail="Company not found")

    db.delete(db_company)
    db.commit()
    return True

@app.post("/chats/", tags=["chat"])
def create_chat(chat: ChatCreate, db: Session = Depends(get_db)):
    db_chat = Chat(**chat.dict())
    db.add(db_chat)
    db.commit()
    db.refresh(db_chat)
    return db_chat

@app.get("/chats/{chat_id}", tags=["chat"])
def read_chat(chat_id: int, db: Session = Depends(get_db)):
    chat = db.query(Chat).filter(Chat.chat_id == chat_id).first()
    if chat is None:
        raise HTTPException(status_code=404, detail="Chat not found")
    return chat

@app.put("/chats/{chat_id}", tags=["chat"])
def update_chat(chat_id: int, chat: ChatUpdate, db: Session = Depends(get_db)):
    db_chat = db.query(Chat).filter(Chat.chat_id == chat_id).first()
    if db_chat is None:
        raise HTTPException(status_code=404, detail="Chat not found")

    update_data = chat.dict(exclude_unset=True)
    if update_data:
        for key, value in update_data.items():
            setattr(db_chat, key, value)
        db.commit()
    return db_chat

@app.delete("/chats/{chat_id}", tags=["chat"])
def delete_chat(chat_id: int, db: Session = Depends(get_db)):
    db_chat = db.query(Chat).filter(Chat.chat_id == chat_id).first()
    if db_chat is None:
        raise HTTPException(status_code=404, detail="Chat not found")

    db.delete(db_chat)
    db.commit()
    return True