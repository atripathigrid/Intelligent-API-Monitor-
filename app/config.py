import os
from pydantic_settings import BaseSettings, SettingsConfigDict

current_file_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_file_path))
env_path = os.path.join(project_root, ".env")


class Settings(BaseSettings):
    DATABASE_URL: str
    API_KEY: str

    #(type + default value)
    MAX_TEMP_THRESHOLD: float = 30.0
    MIN_USD_EUR_THRESHOLD: float = 0.8
    MAX_EARTHQUAKE_MAGNITUDE: float = 5.0

    model_config = SettingsConfigDict(
        env_file=env_path,
        extra="ignore"
    )


settings = Settings()