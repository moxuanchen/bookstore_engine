# -*- coding: utf-8 -*-


class Config():
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = "\xf5\x8elP\x05\xf1\xbb=\xfe'\xabV\x0e\\<\xff\xa1E\xa7%:\x03\x93\x1d"


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///bookstore.db"


class ProdConfig(Config):
    DEBUG = False


def make_config():
    return DevConfig()
