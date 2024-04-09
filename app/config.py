from pydantic_settings import BaseSettings, SettingsConfigDict
#from pydantic import BaseSettings
# try:
class Settings(BaseSettings):
    database_host: str
    database_user: str
    database_password: str
    database_name: str
    database_port: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    # model_config = SettingsConfigDict(env_file='.env', extra='ignore')
    class Config:
        env_file = ".env"
# except PydanticUserError as exc_info:
    # assert exc_info.code == 'config-both'

settings = Settings()
print (settings.database_host)