
from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey
from database import Base


class Task(Base):

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    completed = Column(Boolean, default=False)

    # Connect each task to its owner
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)
