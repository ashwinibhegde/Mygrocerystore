from fastapi import Response, HTTPException, Depends, status, APIRouter
from typing import List
from sqlalchemy.orm import Session


from .. import models, utils
from ..schemas import User, UserBase, CreateUSer
from ..database import get_db

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=List[User])
def user_home(db: Session = Depends(get_db)):
    users = db.query(models.Users).all()
    return users


@router.get("/{id}", response_model=User)
def get_one_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No user with the id {id} exists.",
        )
    return user


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=User)
def create_user(payload: CreateUSer, db: Session = Depends(get_db)):
    hashed_pwd = utils.hash_pwd(payload.password)
    payload.password = hashed_pwd
    new_user = models.Users(**payload.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_one_user(id: str, db: Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.id == id)
    if user.first() == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"There is no user with id {id} exists.",
        )
    user.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", status_code=status.HTTP_201_CREATED, response_model=User)
def update_one_user(id: str, payload: CreateUSer, db: Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.id == id)
    if user.first() == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"There is no user with id {id} exists.",
        )
    user.update(payload.dict(), synchronize_session=False)
    db.commit()
    return user.first()
