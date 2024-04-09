from fastapi import Response, HTTPException, Depends, status, APIRouter
from typing import List
from sqlalchemy.orm import Session

from app import models
from app.schemas import Product, ProductBase, CreateProduct
from app.database import get_db
from ..oauth2 import get_current_user

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/", response_model=List[Product])
def get_all_products(db: Session = Depends(get_db), limit:int = 5):
    products = db.query(models.Products).limit(limit).all()
    return products


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Product)
def create_product(
    payload: CreateProduct,
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user),
):
    new_product = models.Products(owner_id=current_user_id, **payload.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


@router.get("/{id}", response_model=Product)
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    product = db.query(models.Products).filter(models.Products.id == id).first()
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"there are no products for id {id}",
        )
    return product


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(
    id: int,
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user),
):
    product = db.query(models.Products).filter(models.Products.id == id)
    if product.first() == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"there are no products for id {id}",
        )
    if product.first().owner_id != current_user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"the user does not have permission to delete the product ",
        )
    product.delete(synchronize_session=False)
    db.commit()
    # you are not suppose to send any message with response 204 i.e delete
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=Product)
def update_product(
    id: int,
    payload: ProductBase,
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user),
):
    product = db.query(models.Products).filter(models.Products.id == id)
    if product.first() == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"there are no products for id {id}",
        )
    if product.first().owner_id != current_user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"the user does not have permission to update the product. ",
        )
    new_payload = payload.dict()
    new_payload["owner_id"] = current_user_id
    product.update(new_payload, synchronize_session=False)
    # product.update(payload.dict(), synchronize_session=False)
    db.commit()
    return product.first()
