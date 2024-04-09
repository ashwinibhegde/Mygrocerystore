from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time

#from .config import Settings
# url_formate = 'postgresql://<username>:<password>@<hostname>:<port>/<dbname>'

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:****@localhost:5432/fastapi"
#SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_user}:{settings.database_password}@{settings.database_host}:{settings.database_port}/{settings.database_name}"
#print ("##############################", SQLALCHEMY_DATABASE_URL, "##################################")
engine = create_engine(SQLALCHEMY_DATABASE_URL)
LocalSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()

"""host = "localhost"
database = "fastapi"
user = "postgres"
password = "1234"

while True:
    try:
        conn = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            cursor_factory=RealDictCursor,
        )
        cur = conn.cursor()
        print("Database connection is successful.")
        break
    except Exception as error:
        print("Database connection failed.")
        print("Error: ", error)
        time.sleep(2)"""