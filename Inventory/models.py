from .database import Base
from sqlalchemy import Column, Integer, String


class Inventory(Base):
    __tablename__ = "inventory"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    price = Column(String, nullable=False)
    brand = Column(String)