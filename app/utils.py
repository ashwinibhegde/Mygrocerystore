from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_pwd(password: str):
    return pwd_context.hash(password)


def pwd_verify(password, Hashed_password):
    return pwd_context.verify(password, Hashed_password)
