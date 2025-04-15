from sqlalchemy import Column, String, ForeignKey
from app.models.base import Base


class Board(Base):
    __tablename__ = "boards"

    id = Column(String(36), primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    content = Column(String(1000))
    user_id = Column(String(36), ForeignKey("users.id"))