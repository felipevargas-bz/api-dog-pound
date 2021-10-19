from sqlalchemy.orm import Session
from models import dog as dog_model
from schemas import dog as dog_schema
from fastapi import HTTPException
from datetime import datetime


def get_dog(name: str, db: Session):
    """get dog with the name"""
    return db\
        .query(dog_model.Dog)\
        .filter(dog_model.Dog.name == name)\
        .first()


def get_dogs(db: Session):
    """get all dogs"""

    return db.query(dog_model.Dog).all()


def create_dog(db: Session, dog: dog_schema.DogCreate):
    """create a dog"""
    db_dog = dog_model.Dog(
        name=dog.name,
        picture=dog.picture,
        is_adopted=dog.is_adopted,
        id_user=dog.id_user,
        create_date=dog.create_date,
        update_date=dog.create_date
    )
    try:
        db.add(db_dog)
        db.commit()
        db.refresh(db_dog)

        return {"message": "Dog is Created!"}
    except Exception as e:
        return {
            "message": "Internal server Error -- Error: {} ---".format(e)
        }


def update_dog(
    name: str,
    dog: dog_schema.Dog,
    db: Session
):
    """update a record (dog) by name"""
    dog_update = db.query(dog_model.Dog)\
        .filter(dog_model.Dog.name == name)\
        .first()
    if not dog_update:
        raise HTTPException(
            status_code=404,
            detail="Dog not found"
        )

    dog_update.name = dog.name
    dog_update.is_adopted = dog.is_adopted
    dog_update.update_date = datetime\
        .now()\
        .strftime('%b %dth, %Y - %H:%M hrs')

    db.commit()

    return {"message": "Dog is updated!"}


def delete_user(name: str, db: Session):
    """Delete a record (dog) by name"""
    dog = db\
        .query(dog_model.Dog)\
        .filter(dog_model.Dog.name == name)\
        .first()
    if not dog:
        raise HTTPException(status_code=404, detail="Dog not found")

    db.delete(dog)
    db.commit()
    return {'message': 'Dog is deleted!'}
