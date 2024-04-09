from fastapi import Response, HTTPException, Depends, status, APIRouter
from typing import List
from sqlalchemy.orm import Session

from app import models
from app.schemas import Product, ProductBase, CreateProduct, Rating
from app.database import get_db
from ..oauth2 import get_current_user

router = APIRouter(prefix="/ratings", tags=["ratings"])

@router.get("/", response_model=List[Rating])
def get_all_ratings(db: Session = Depends(get_db)):
    ratings = db.query(models.Ratings).all()
    return ratings

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Rating)
def create_ratings(payload:Rating, db: Session = Depends(get_db), current_user_id = Depends(get_current_user)):
    #product = db.query(models.Products).filter(models.Products.id == payload.product_id).first()
    #new_rating["user_id"] = current_user_id
    #new_rating["product_name"] = product
    #payload.user_id = current_user_id
    #payload.product_name = product
    #print (product)
    new_rating = models.Ratings(**payload.model_dump())
    print ("############################", new_rating, "###########################")
    db.add(new_rating)
    db.commit()
    db.refresh(new_rating)
    return new_rating
