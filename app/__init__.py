import os

from flask import Flask
from flask_mail import Mail


mail = Mail()


def create_app(config=None):

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(SECRET_KEY=os.environ.get("FLASK_SECRETS", "dev"))

    from .views import bp as home_blueprint

    app.register_blueprint(home_blueprint)

    if config:
        app.config.from_mapping(config)
    else:
        app.config.from_pyfile("config.py", silent=True)

    app.config["MAIL_SERVER"] = os.environ.get(
        "FLASK_MAIL_SERVER", "mail.privateemail.com"
    )
    app.config["MAIL_PORT"] = os.environ.get("FLASK_MAIL_PORT", 465)
    app.config["MAIL_USERNAME"] = os.environ.get("FLASK_MAIL_USERNAME", "test@gmail.com")
    app.config["MAIL_PASSWORD"] = os.environ.get("FLASK_MAIL_PASSWORD", "test_password")
    app.config["MAIL_USE_TLS"] = False
    app.config["MAIL_USE_SSL"] = True

    mail.init_app(app)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app


app = create_app()
