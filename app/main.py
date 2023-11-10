from fastapi import FastAPI
from sqlalchemy import create_engine
from models.base import Base
from models.user import User
from models.chat import Chat
from models.admin_panel_logs import AdminPanelLogs
from models.screen_share import ScreenShare
from models.video_call import VideoCall
from models.companies import Company
from models.order_items import OrderItem
from models.product import Product
from models.order import Order

app = FastAPI()

engine = create_engine("postgresql+pg8000://root:root@localhost:5432/product_db", echo=True)
Base.metadata.create_all(engine)

