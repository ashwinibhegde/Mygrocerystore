from .database import Base
from sqlalchemy import Column, Integer, String, BOOLEAN, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship


class Products(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    cost = Column(Integer, nullable=False)
    is_available = Column(BOOLEAN, server_default="TRUE", nullable=False)
    size = Column(String, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    owner_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )

    owner = relationship("Users")


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    age = Column(Integer)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )


class Ratings(Base):
    __tablename__ = "ratings"
    product_id = Column(Integer, ForeignKey(column="products.id", ondelete="CASCADE"), primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey(column="users.id", ondelete="CASCADE"), primary_key=True, nullable=False)
    rating = Column(Integer)
    product_name = Column(String)


#does he know these people
#from where did they get the house details