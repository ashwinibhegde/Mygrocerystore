from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from ..database import get_db
from .. import models
from .. import schemas
from .. import utils
from ..oauth2 import create_access_token

router = APIRouter(prefix="/login", tags=["auth"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Token)
# def login(payload: schemas.UserLogin, db: Session = Depends(get_db)):
def login(
    user_credentials: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    try:
        user = (
            db.query(models.Users)
            .filter(models.Users.email == user_credentials.username)
            .first()
        )
        if not user:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials."
            )
        verify = utils.pwd_verify(user_credentials.password, user.password)
        if not verify:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials."
            )
        jwt_token = create_access_token({"user_id": user.id})
        return {"access_token": jwt_token, "token_type": "bearer"}
    except Exception as e:
        print("error is: ", e)
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials."
        )
