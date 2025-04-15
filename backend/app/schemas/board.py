from pydantic import BaseModel


class BoardBase(BaseModel):
    title: str
    content: str


class BoardCreate(BoardBase):
    user_id: str


class BoardRead(BoardBase):
    id: str
    user_id: str

    class Config:
        orm_mode = True