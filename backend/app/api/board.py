from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.board import BoardCreate, BoardRead
from app.services.board import create_board, get_board
from app.core.db import get_db

router = APIRouter(prefix="/boards")


@router.post("/", response_model=BoardRead)
def create(board: BoardCreate, db: Session = Depends(get_db)):
    return create_board(db, board)


@router.get("/{board_id}", response_model=BoardRead)
def read(board_id: str, db: Session = Depends(get_db)):
    return get_board(db, board_id)