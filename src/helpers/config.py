from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str
    OPENAI_API_KEY: str
    FILE_UPLOAD_EXTENSTION: list
    FILE_MAX_SIZE: int

    class Config:
        env_file = ".env"

def get_settings():
    return Settings()

