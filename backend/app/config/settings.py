# Purpose -> Reads .env, defines application settings, database..
from pydantic_settings import BaseSettings, SettingsConfigDict

# lru_cache will make it the object (Settings) is only created once from config file
 # lru_cache makes it that the function returns the same value that was returned the first time
from functools import lru_cache


class Settings(BaseSettings):
    # contains everything we need for our database (app setting)
    DATABASE_URL: str
    
    # tells pydantic how to load settings
        # scans env file and automatically matches value that matches field we defined
    model_config = SettingsConfigDict(env_file =".env")

    
@lru_cache
def get_settings():
    return Settings()