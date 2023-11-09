from pydantic import BaseSettings

class settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str = "postgresql+pg8000://root:root@localhost:5432/product_db"


settings = settings()
