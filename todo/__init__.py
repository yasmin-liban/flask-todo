from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api


db = SQLAlchemy()
migrate = Migrate()
api = Api()

def init_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)
    
    with app.app_context():
        # Import all app models here
        from .models import (Todo)

        # from . import routes
        # app.register_blueprint(auth.auth_bp)
        # app.register_blueprint(admin.admin_bp)
        db.create_all()
        return app