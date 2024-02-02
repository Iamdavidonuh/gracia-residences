import os

from flask import Flask
from . import views

def create_app(config=None):

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(SECRET_KEY=os.environ.get("FLASK_SECRETS", "dev"))

    app.register_blueprint(views.bp)

    if config:
        app.config.from_mapping(config)
    else:
        app.config.from_pyfile("config.py", silent=True)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app


app = create_app()
