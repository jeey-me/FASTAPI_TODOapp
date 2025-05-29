# models.py

from sqlalchemy import Column, Integer, Boolean, Text
from database import Base

#ORM으로 DB에 테이블을 만들기 위한 클래스 정의 
class Todo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True)
    task = Column(Text)
    completed = Column(Boolean, default=False)