from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, Query

from app.config.settings import get_settings

# ---- Main Application ---- #

app = FastAPI()

