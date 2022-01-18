from . import db
from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func

class Todo(db.Model):
    __tablename__= "todo"
    id = Column(Integer, primary_key=True)
    title = Column(String(100), unique=False, nullable=True)
    description = Column(String(320), unique=False, nullable=True)
    done = Column(Boolean(), default=False)
    created = Column(DateTime(), server_default=func.now())
    edited = Column(DateTime(), server_default=func.now() , onupdate=func.now())

    def __repr__(self):
        return "<Todo 🞄 {}>"