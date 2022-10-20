from flask import Flask

from .extensions import db
from .views import views

def create_app(config_file='settings.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///score_db.db'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from . import models

    with app.app_context():
        db.create_all()

    app.register_blueprint(views)

    return app

    