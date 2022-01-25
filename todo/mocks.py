from flask import Blueprint
import click
from todo.models import db, Todo

todos_bp = Blueprint('mock_todos', __name__)

data = [
    {
        "title": "Finish my First Flask App",
        "description": "Finish this project of a Flask App I started"
    },
    {
        "title": "Drink my meds",
        "description": "Don't forget your meds huh",
        "done": True
    }
]

@todos_bp.cli.command('create')
def create_todos():
    for d in data:
        new_data = Todo(
            title=d.get("title",""), 
            description=d.get("description",""), 
            done=d.get("done", False)
        )
        db.session.add(new_data)
        db.session.commit()