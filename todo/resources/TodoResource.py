from typing import Union
from flask import request
from flask_restful import Resource
from todo.models import Todo


class TodoResource(Resource):
    def get(self, id:Union[int, None]=None):
        # try:
        #     todo = Todo.query.get(id)
        pass
    
    def post(self):
        pass
    
    def put(self, id:Union[int, None]=None):
        pass
    
    def delete(self, id:Union[int, None]=None):
        pass
    
    def patch(self, id:Union[int, None]=None):
        pass
    
    def put(self, id:Union[int, None]=None):
        pass