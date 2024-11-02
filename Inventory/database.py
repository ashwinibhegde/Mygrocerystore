from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


from app import config
# url_formate = 'postgresql://<username>:<password>@<hostname>:<port>/<dbname>'
db_user = config.database_user
print ("db_user:", db_user)
db_host = config.database_host
db_pw = config.database_password
db_port = config.database_port
db_name = config.database_name

#SQLALCHEMY_DATABASE_URL = "postgresql://postgres:****@localhost:5432/fastapi"
SQLALCHEMY_DATABASE_URL = f"postgresql://{db_user}:{db_pw}@{db_host}:{db_port}/{db_name}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
LocalSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()