from pydantic import BaseModel


class UserBase(BaseModel):
    name: str


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    id: str

    class Config:
        orm_mode = True