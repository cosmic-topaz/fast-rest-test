from sqlalchemy.orm import Session
from app.models.board import Board
from app.schemas.board import BoardCreate
import uuid


def create_board(db: Session, board: BoardCreate):
    db_board = Board(id=str(uuid.uuid4()), **board.dict())
    db.add(db_board)
    db.commit()
    db.refresh(db_board)
    return db_board


def get_board(db: Session, board_id: str):
    return db.query(Board).filter(Board.id == board_id).first()