# -*- conding: utf-8 -*-

from core.database import db


class Book(db.Model):
    __tablename__ = "book"
    id = db.Column(db.Integer, primary_key=True)
    name_en = db.Column(db.String(256), nullable=False)
    name_ch = db.Column(db.String(256), nullable=False)
    tag_id = db.Column(db.String(1024), nullable=True)
    comment = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)
    cover = db.Column(db.String(256), nullable=True)
