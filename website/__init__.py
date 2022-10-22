import imp
from flask import Flask

# from data_control_score_system import Score

from .extensions import db
from .views import views

def create_app(config_file='settings.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(views)

    return app

    