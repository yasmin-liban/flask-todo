from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
migrate = Migrate()
api = Api()
ma = Marshmallow()

def init_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)
    ma.init_app(app)

    with app.app_context():
        
        # Import all app models here
        from .models.TodoModel import (Todo)
        from .mocks.TodoMocks import todos_bp

        # Blueprints
        app.register_blueprint(todos_bp)
        
        # APIs Resources

        db.create_all()
        return app