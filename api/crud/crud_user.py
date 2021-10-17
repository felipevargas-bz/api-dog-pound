from sqlalchemy.orm import Session
from models import user as user_model
from schemas import user as user_schema


def get_user(user_email: str, db: Session):
    """get user by email"""
    return db\
        .query(user_model.User)\
        .filter(user_model.User.email == user_email)\
        .first()


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
