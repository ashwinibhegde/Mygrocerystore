import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()
database_host = os.getenv("DATABSE_HOST")
database_user = os.getenv("DATABSE_USER")
database_password = os.getenv("DATABSE_PASSWORD")
database_name = os.getenv("DATABSE_NAME")
database_port = os.getenv("DATABASE_PORT")
secret_key = os.getenv("SECRET_KEY")
algorithm = os.getenv("ALGORITHM")
access_token_expire_minutes = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


#config = dotenv_values(".env")
#print(config['DATABSE_HOST'])

