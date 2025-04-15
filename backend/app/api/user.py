from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserRead
from app.services.user import create_user, get_user
from app.core.db import get_db

router = APIRouter(prefix="/users")


@router.post("/", response_model=UserRead)
def create(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)


@router.get("/{user_id}", response_model=UserRead)
def read(user_id: str, db: Session = Depends(get_db)):
    return get_user(db, user_id)