from flask import Flask

from .extensions import db

from .view_score import view_score
from .view_team import view_team
from .view_time import view_time

from .views import views


def create_app(config_file='settings.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(view_score)
    app.register_blueprint(view_team)
    app.register_blueprint(view_time)

    app.register_blueprint(views)

    return app

    