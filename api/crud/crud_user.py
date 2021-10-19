from sqlalchemy.orm import Session
from models import user as user_model
from schemas import user as user_schema
from fastapi import Depends, HTTPException
from datetime import datetime


def get_user(user_email: str, db: Session):
    """get user by email"""
    return db\
        .query(user_model.User)\
        .filter(user_model.User.email == user_email)\
        .first()


def update_user(
    user_email: str,
    user: user_schema.User,
    db: Session
):
    """update user by email"""
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

    return {"message": "User is updated!"}


def get_users(db: Session):
    """get all users"""
    return db.query(user_model.User).all()


def create_user(db: Session, user: user_schema.UserCreate):
    """create a user"""
    db_user = user_model.User(
        name=user.name,
        last_name=user.last_name,
        email=user.email,
        create_date=user.create_date,
        update_date=user.create_date
    )
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return {"message": "User  is Created!"}
    except Exception as e:
        return {"message": "Internal server Error -- Error: {} ---".format(e)}


def delete_user(
    user_email: str,
    db: Session
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
