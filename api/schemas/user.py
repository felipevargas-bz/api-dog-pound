from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    """schema for user model"""

    name: str
    last_name: str
    email: str
    create_date: str = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    update_date: str = create_date


class UserCreate(UserBase):
    pass


class User(UserBase):
    """..."""
    id: int

    class Config:
        orm_mode = True
