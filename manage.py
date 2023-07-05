from app import create_app
from app.extensions import db, migrate, login, seeder, manager

manager.add_command('seed_database', seeder)

@manager.shell
def make_shell_context():
    return dict(app=create_app(), db=db)

if __name__ == '__main__':
    manager.run()
