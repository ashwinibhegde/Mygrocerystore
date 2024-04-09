from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Optional



class UserBase(BaseModel):
    name: str
    age: Optional[int]
    email: EmailStr
    password: str


class CreateUSer(UserBase):
    pass


class User(BaseModel):
    name: str
    age: Optional[int]
    email: EmailStr
    id: int

    class Config:
        orm_model = True
class ProductBase(BaseModel):
    name: str
    cost: int
    size: str
    is_available: bool = True


class CreateProduct(ProductBase):
    pass


class Product(ProductBase):
    id: int
    owner_id: int
    owner: User
    # model_config = ConfigDict(arbitrary_types_allowed=True)
    class Config:
        orm_model = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str]

class Rating(BaseModel):
    product_id: int
    user_id: Optional[int]
    product_name: Optional[str]
    rating: int

    class Config:
        orm_model = True
