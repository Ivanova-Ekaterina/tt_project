#! /Users/ekaterina/Documents/track/backend/tt_project/venv/bin/python3

from app import app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
@manager.command
def hello():
    print("Hello")

if __name__ == "__main__":
    manager.run()
    #app.run()
