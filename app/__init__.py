from flask import Flask, render_template
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app.models import animal
from app.database import db


# login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    migrate = Migrate()
    migrate.init_app(app, db)
    db.init_app(app)

    from app.blueprints.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.blueprints.auth import bp as auth_bp 
    app.register_blueprint(auth_bp)


    return app
