from app import create_app
from flask_script import Manager,Server
from app.model import User,Role
from app import db
from flask_migrate import Migrate, MigrateCommand

# .....


app =create_app('development')

manager=Manager(app)
manager.add_command('server',Server)

# if __name__=='__main__':
#     manager.run()

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

   
@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User,Role = Role)
if __name__ == '__main__':
    manager.run()