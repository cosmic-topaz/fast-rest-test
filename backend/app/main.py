import os

from fastapi import FastAPI
from app.api import user, board

app = FastAPI()

app.include_router(user.router)
app.include_router(board.router)

@app.get("/")
def read_root():
    return {
        "message": "Hello world",
        "db_host": os.getenv("MYSQL_HOST")
    }


# uvicorn app.main:app --reload

# Directory structure
# 
# backend
# ├── app
# │   ├──main.py
# 


