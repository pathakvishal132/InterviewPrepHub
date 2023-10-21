from flask import Flask
from application.database import db
from flask_login import LoginManager


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    app.secret_key = "33879e5f6102c4d083b79821a6f7111a"
    db.init_app(app)
    login_manager = LoginManager(app)
    login_manager.login_view = "login_page"
    login_manager.login_message_category = "info"

    app.app_context().push()

    return app


app = create_app()

from application.controller import *


if __name__ == "__main__":
    db.create_all()
    app.run(host="0.0.0.0", port=2345, debug=True)
