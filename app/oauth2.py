from jose import jwt, JWTError
from datetime import timedelta, datetime
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, status, HTTPException

from . import config

# SECRET KEY
# ALGORITHM
# EXPIRATION TIME

# openssl rand -hex 32
SECRET_KEY = config.secret_key
ALGORITHM = config.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = config.access_token_expire_minutes

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def create_access_token(payload: dict):
    to_encode = payload.copy()
    expire = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES) + datetime.utcnow()
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_access_token(token: str, credential_exception):
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        id: str = decoded_token.get("user_id")
        if id is None:
            raise credential_exception
    except JWTError:
        raise credential_exception
    return id


def get_current_user(token: str = Depends(oauth2_scheme)):
    credential_exception = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Credentials are not valid."
    )
    return verify_access_token(token, credential_exception)
