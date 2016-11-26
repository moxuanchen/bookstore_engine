# -*- coding: utf-8 -*-

from flask_script import Manager, Server
from flask_migrate import MigrateCommand
from core.app import create_app

manage = Manager(create_app())


if __name__ == "__main__":
    manage.add_command('server', Server)
    manage.add_command('db', MigrateCommand)
    manage.run()
