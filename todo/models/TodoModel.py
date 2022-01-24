from flask_sqlalchemy import Model
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.sql import func
from passlib.hash import bcrypt

class Todo(Model):
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True)
    title = Column(String(100), unique=False, nullable=True)
    description = Column(String(320), unique=False, nullable=True)
    done = Column(Boolean(), default=False)
    created = Column(DateTime(), server_default=func.now())
    edited = Column(DateTime(), server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return "<Todo 🞄 {}>"

class User(Model):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True)
    name = Column(String(200), unique=False, nullable=False)
    _password = Column(String(100), nullable=False)

    def __repr__(self):
        return "<User 🞄 {}>"
    
    @hybrid_property
    def password(self, password):
        hasher = bcrypt.using(rounds=13)
        return hasher.hash(password)