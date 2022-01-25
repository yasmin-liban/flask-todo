from todo import db
from flask_sqlalchemy import Model
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.sql import func
from passlib.hash import bcrypt

class BaseMixin(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
    
    id =  Column(Integer, primary_key=True, autoincrement=True)
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        self.query.get(self.id).delete()

class Todo(Model, BaseMixin):
    title = Column(String(100), unique=False, nullable=True)
    description = Column(String(320), unique=False, nullable=True)
    done = Column(Boolean(), default=False)
    created = Column(DateTime(), server_default=func.now())
    edited = Column(DateTime(), server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return "<Todo 🞄 {}>"

class User(Model, BaseMixin):
    email = Column(String(100), unique=True)
    name = Column(String(200), unique=False, nullable=False)
    password = Column(String(100), nullable=False)

    def __repr__(self):
        return "<User 🞄 {}>"
    
    @hybrid_property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, password):
        hasher = bcrypt.using(rounds=13)
        self.password = hasher.hash(password)