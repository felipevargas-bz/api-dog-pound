from sqlalchemy.orm import Session
from models import dog as dog_model
from schemas import dog as dog_schema

def get_dog(name: str, db: Session):
    return db.query(dog_model.Dog).filter(dog_model.Dog.name == name).first()


def get_dogs(db: Session):
    return db.query(dog_model.Dog).all()


def create_dog(db: Session, dog: dog_schema.DogCreate):
    db_dog = dog_model.Dog(
        name=dog.name,
        picture=dog.picture,
        is_adopted=dog.is_adopted,
        create_date=dog.create_date
    )
    try:
        db.add(db_dog)
        db.commit()
        db.refresh(db_dog)
    except:
        return {"message": "Internal server Error"}
    return {"message": "OK"}
