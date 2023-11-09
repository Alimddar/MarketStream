from alembic.config import Config
from alembic import command

from app.models.user import Base

from app.models.admin_panel_logs import AdminPanelLogs
from app.models.chat import Chat
from app.models.companies import Company
from app.models.order_items import OrderItem
from app.models.order import Order
from app.models.product import Product
from app.models.screen_share import ScreenShare
from app.models.user import User
from app.models.video_call import VideoCall

from app.core.config import settings

alembic_cfg = Config("alembic.ini")
alembic_cfg.set_main_option("sqlalchemy.url", settings.SQLALCHEMY_DATABASE_URL)

command.revision(alembic_cfg, autogenerate=True, message="generate new migration")

command.upgrade(alembic_cfg, "head")
