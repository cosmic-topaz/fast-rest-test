# backend/app/db/base.py
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass


# 모든 모델은 다 Base를 상속해서 정의해야 함
