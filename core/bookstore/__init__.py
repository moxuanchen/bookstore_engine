# -*- coding: utf-8 -*-

from flask import Blueprint

blueprint = Blueprint("bookstore", __name__, template_folder="../templates", static_folder="static")

from . import bookstore_views
