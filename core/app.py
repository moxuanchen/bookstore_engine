# -*- coding: utf-8 -*-

from flask import Flask
from settings import make_config
from bookstore import bookstore_views
from core.database import db, migrate


def create_app(config=make_config()):
    app = Flask(__name__)
    db.init_app(app)
    migrate.init_app(app, db)
    app.config.from_object(config)
    app.secret_key = app.config["SECRET_KEY"]
    register_blueprints(app)
    return app


def register_blueprints(app):
    app.register_blueprint(bookstore_views.blueprint)
