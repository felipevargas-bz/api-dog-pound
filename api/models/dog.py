from sqlalchemy import Column
from datetime import datetime
from sqlalchemy.sql.sqltypes import Boolean, DateTime, Integer, String
from internal.admin import Base


class Dog(Base):
    """Define a dog with its attributes in SQLAlchemy."""

    __tablename__ = "dogs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True)
    picture = Column(String(500))
    is_adopted = Column(Boolean)
    create_date = Column(String(30))
