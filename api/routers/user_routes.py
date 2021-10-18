"""
define the routes of our api,
working with the scheme below.
    ___________User___________
    |+ id: integer          |
    |+ name: String         |
    |+ last_name: String    |
    |+ email: String        |
    |+ update_date: String  |
    |+ create_date: String  |
"""
from re import S
from fastapi import APIRouter
from typing import List
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import user as user_schema
from models import user as user_model
from models import dog as dog_model
from crud import crud_user
from internal.admin import SessionLocal
from datetime import datetime


router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get(
    "/api/users",
    response_model=List[user_schema.User],
    status_code=200
)
async def get_users(db: Session = Depends(get_db)):
    """Get a list of all users"""
    users = crud_user.get_users(db)
    return users


@router.get("/api/users/{user_email}")
async def get_user(
    user_email: str,
    db: Session = Depends(get_db)
):
    """get user by email"""
    return crud_user.get_user(user_email=user_email, db=db)


@router.get("/api/users/dogs/{user_email}")
async def user_dogs(user_email: str, db: Session = Depends(get_db)):
    """Get all the dogs of an user"""

    user_dogs: List = []
    user = crud_user.get_user(user_email=user_email, db=db)
    dogs = db.query(dog_model.Dog).all()

    for dog in dogs:
        if dog.id_user == user.id:
            user_dogs.append(dog)
    if user_dogs == []:
        return {"message": "The user does not have any registered dogs."}
    return user_dogs


@router.post("/api/users/{user_email}")
async def create_user(
    user_email: str,
    user: user_schema.UserCreate,
    db: Session = Depends(get_db)
):
    """create an user by email"""
    user.email = user_email
    return crud_user.create_user(db=db, user=user)


@router.put("/api/users/{user_email}")
async def update_user(
    user_email: str,
    user: user_schema.User,
    db: Session = Depends(get_db)
):
    """update an user"""
    user_update = db.query(user_model.User)\
        .filter(user_model.User.email == user_email)\
        .first()
    if not user_update:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    user_update.name = user.name
    user_update.last_name = user.last_name
    user_update.email = user.email
    user_update.update_date = datetime\
        .now()\
        .strftime('%b %dth, %Y - %H:%M hrs')

    db.commit()

    return user_update


@router.delete("/api/users/{user_email}")
async def delete_user(
    user_email: str,
    db: Session = Depends(get_db)
):
    """delete user by email"""
    user = db.query(user_model.User)\
        .filter(user_model.User.email == user_email)\
        .first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return {"message": 'User is deleted!'}
