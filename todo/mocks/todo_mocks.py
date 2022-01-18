from typing import List
from todo.models import db, Todo

data = [
    {
        "title": "Finish my First Flask App",
        "descripton": "Finish this project of a Flask App I started"
    },
    {
        "title": "Drink my meds",
        "descripton": "Don't forget your meds huh",
        "done": True
    }
]

def save_data(data: list[dict]):
    for d in data:
        new_data = Todo(
            title=d.get("title",""), 
            description=d.get("description",""), 
            done=d.get("done", False)
        )
        db.session.add(new_data)
        db.session.commit()

save_data(data)