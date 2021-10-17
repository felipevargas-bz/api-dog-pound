from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from internal.admin import Base


class User(Base):
    """Define a user with its attributes in SQLAlchemy."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(40))
    last_name = Column(String(40))
    email = Column(String(80), unique=True)
    create_date = Column(String(30))
    update_date = Column(String(30))

    dog = relationship("Dog", back_populates="owner", cascade="all, delete-orphan")