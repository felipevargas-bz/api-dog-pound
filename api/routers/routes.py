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
from fastapi.params import Depends
from sqlalchemy.orm import Session
from schemas  import dog as dog_schema
from crud import crud_dog
from internal.admin import SessionLocal


router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/api/dogs", response_model=List[dog_schema.Dog], status_code=200)
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
async def update_dog(name: str):
    """Update a record (dog) by name"""
    return {"message": "update dog with name {}".format(name)}


@router.delete("/api/dogs/{name}")
async def delete_dog(name: str):
    """Delete a record (dog) by name."""
    return {"message": "delete dog with name {}".format(name)}


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

    return crud_dog.create_dog(db=db, dog=dog)


@router.get("/api/dogs/{name}")
async def get_dog_name(name: str):
    """Get an input (a dog) from the name"""
    return {"message": "get dog with name {}".format(name)}
