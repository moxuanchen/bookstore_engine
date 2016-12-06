# -*- conding: utf-8 -*-

from core.database import db


class User(db.Model):
    __tablename__ = "User"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(24), nullable=False)
    email = db.Column(db.String(36), nullable=False)
    password = db.Column(db.String(24), nullable=False)
    active = db.Column(db.Boolean(), nullable=False, default=True)
    created_at = db.Column(db.DateTime(), nullable=False)
