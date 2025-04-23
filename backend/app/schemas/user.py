from pydantic import BaseModel


class UserBase(BaseModel):
    id: int
    name: str
    
    class Config:
        from_attributes = True # Pydantic v2.x에서 사용되는 설정




class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    
    class Config:
        from_attributes = True # Pydantic v2.x에서 사용되는 설정
        