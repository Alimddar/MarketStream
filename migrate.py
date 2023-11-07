from alembic.config import Config
from alembic import command
from app.core.config import settings

alembic_cfg = Config("alembic.ini")

alembic_cfg.set_main_option("sqlalchemy.url", settings.SQLALCHEMY_DATABASE_URL)

command.revision(alembic_cfg, autogenerate=True, message="generate new migration")

command.upgrade(alembic_cfg, "head")
