from flask_migrate import Migrate
from flask_migrate import MigrateCommand

from flask_script import Manager
from settings import app_instance
from settings import db
migrate = Migrate(app_instance, db)
managers_script = Manager(app_instance)
managers_script.add_command('db', MigrateCommand)

if __name__ == '__main__':
    app_instance.run(host='0.0.0.0')

