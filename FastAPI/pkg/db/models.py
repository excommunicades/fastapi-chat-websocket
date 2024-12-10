from sqlalchemy import Column, String, Integer

from FastAPI.pkg.db.database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, unique=True, primary_key=True, nullable=False)

    username = Column(String(30), nullable=False)

    email = Column(String(100), unique=True, nullable=False)

    password = Column(String(255), nullable=False)
