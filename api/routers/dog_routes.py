"""
define the routes of our api,
working with the scheme below.
    ___________Dog___________
    |+ id: integer          |
    |+ name: String         |
    |+ picture: String      |
    |+ is_adopted: Boolean  |
    |+ create_date: Datetime|
"""
from typing import List
from fastapi import APIRouter
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import dog as dog_schema
from models import dog as dog_model
from crud import crud_dog
from internal.admin import SessionLocal
from utils.get_picture import get_picture


router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get(
    "/api/dogs", response_model=List[dog_schema.Dog], status_code=200)
async def get_dogs(db: Session = Depends(get_db)):
    """Get a list of all dogs"""
    dogs = crud_dog.get_dogs(db)
    return dogs


@router.get("/api/dogs/is_adopted", response_model=List[dog_schema.Dog], status_code=200)
async def dogs_is_adopted(db: Session = Depends(get_db)):
    """Get all inputs (dogs) where the is_adopted flag is >> True."""
    dogs = crud_dog.get_dogs(db)
    dog_adopted: List = []
    for dog in dogs:
        if dog.is_adopted:
            dog_adopted.append(dog)
    return dog_adopted


@router.put("/api/dogs/{name}")
async def update_dog(name: str, dog: dog_schema.Dog, db: Session = Depends(get_db)):
    """Update a record (dog) by name"""
    dog_update = db.query(dog_model.Dog).filter(
        dog_model.Dog.name == name).first()
    if not dog_update:
        raise HTTPException(status_code=404, detail="Dog not found")

    dog_update.name = dog.name
    dog_update.description = dog.is_adopted

    db.commit()

    return dog_update


@router.delete("/api/dogs/{name}")
async def delete_dog(name: str, db: Session = Depends(get_db)):
    """Delete a record (dog) by name."""
    dog = db.query(dog_model.Dog).filter(dog_model.Dog.name == name).first()
    if not dog:
        raise HTTPException(status_code=404, detail="Dog not found")

    db.delete(dog)
    db.commit()
    return {'message': 'Dog is deleted!'}


@router.post("/api/dogs/{name}", status_code=201)
async def post_dogs(
    *,
    name: str,
    dog: dog_schema.DogCreate,
    db: Session = Depends(get_db)
):
    """
    Save a record according to the scheme
    """
    dog.name = name
    dog.picture = get_picture()
    return crud_dog.create_dog(db=db, dog=dog)


@router.get("/api/dogs/{name}")
async def get_dog_name(name: str, db: Session = Depends(get_db)):
    """Get an input (a dog) from the name"""
    return crud_dog.get_dog(name=name, db=db)
