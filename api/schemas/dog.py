from pydantic import BaseModel
from datetime import datetime


class DogBase(BaseModel):
    """schema for dog model"""

    name: str
    picture: str
    is_adopted: bool
    create_date: datetime


class DogCreate(DogBase):
    pass


class Dog(DogBase):
    """..."""
    id: int

    class Config:
        orm_mode = True
