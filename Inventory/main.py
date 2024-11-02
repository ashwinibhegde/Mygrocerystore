from fastapi import FastAPI, Depends
from typing import Optional
from pydantic import BaseModel
from . import models
from .database import engine
from .database import get_db
from sqlalchemy.orm import Session
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/inventory")
def get_inventory(db: Session = Depends(get_db)):
    return {"status": "Success"}



my_inventory_list = {
    "item1":
        {"name":"Bed", "price": 200.00, "brand": "Ikea"},
    "item2":
        {"name": "Phone", "price": 700.00, "brand": "Apple"}
}

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None



@app.get("/home/{item}")
def my_home(item:str):
    return my_inventory_list[item]

@app.get("/items")
def my_items(*, name: str):
    for each in my_inventory_list:
        if my_inventory_list[each]["name"] == name:
            return my_inventory_list[each]

#post
@app.post("/create")
def create_item(item_id:str, item: Item):
    if item_id in my_inventory_list:
        return {"Error": "Item already exists in the inventory list"}
    my_inventory_list[item_id] = item
    return my_inventory_list[item_id]

@app.put("/update")
def update_item(item_id:str, item: UpdateItem):
    print ("#########################################################")
    print (item.name)
    print("#########################################################")
    if item_id not in my_inventory_list:
        return {"Error": f"No Item with the item id {item_id} found"}
    if item.name != None:
        my_inventory_list[item_id]["name"] = item.name
    if item.price != None:
        my_inventory_list[item_id]["price"] = item.price
    if item.brand != None:
        my_inventory_list[item_id]["brand"] = item.brand
    return my_inventory_list[item_id]

@app.delete("/delete")
def delete_item(item_id: str):
    if not item_id in my_inventory_list:
        return {"Error": f"Item ID {item_id} does not exist"}
    del my_inventory_list[item_id]
    return {"Message": f"Item with the item ID {item_id} has been deleted from the inventory"}

