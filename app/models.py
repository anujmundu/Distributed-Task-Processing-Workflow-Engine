from sqlalchemy import Column, String, Integer, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Task(Base):
    __tablename__ = "tasks"

    id = Column(String, primary_key=True)
    status = Column(String)
    attempts = Column(Integer, default=0)
    payload = Column(JSON)
    result = Column(JSON, nullable=True)
