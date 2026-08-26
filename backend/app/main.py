# We want it so that the configuration is loaded once and reused consistently rather than reconsutrcting it completely

from fastapi import FastAPI

from app.config.settings import get_settings

# ---- Main Application ---- #

app = FastAPI()



test = get_settings()
print(test)