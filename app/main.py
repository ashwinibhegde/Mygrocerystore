from fastapi import FastAPI, Depends

from . import models
from .database import engine
from .routers import products, users, auth, ratings

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(products.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(ratings.router)


@app.get("/")
def home():
    return {"message": "Hello World"}
