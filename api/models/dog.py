from sqlalchemy import Column, Boolean, Integer, String
from sqlalchemy.orm import backref, relationship
from sqlalchemy.sql.schema import ForeignKey
from internal.admin import Base
from models.user import User


class Dog(Base):
    """Define a dog with its attributes in SQLAlchemy."""

    __tablename__ = "dogs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True)
    picture = Column(String(500))
    is_adopted = Column(Boolean)
    create_date = Column(String(30))
    update_date = Column(String(30))
    id_user = Column(Integer, ForeignKey('users.id'))

    owner = relationship("User", back_populates="dog")
