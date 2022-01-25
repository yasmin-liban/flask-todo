from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from .models import Todo
from flask_marshmallow.fields import Hyperlinks, URLFor
from marshmallow import Schema
from marshmallow.fields import Int

class TodoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Todo
    
    id = auto_field()
    title = auto_field()
    description = auto_field()
    done = auto_field()
    created = auto_field()
    edited = auto_field()

    links = Hyperlinks(
        {
            "self": URLFor("get_todo", values=dict(id="<id>")),
            "collection": URLFor("all_todo"),
        }
    )

class PaginationSchema(Schema):
   page = Int(missing=1)
   limit = Int(missing=8)