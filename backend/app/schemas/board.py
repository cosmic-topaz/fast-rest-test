from pydantic import BaseModel


class BoardBase(BaseModel):
    title: str
    content: str


class BoardCreate(BoardBase):
    user_id: str


class BoardRead(BoardBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True # Pydantic v2.x에서 사용되는 설정
