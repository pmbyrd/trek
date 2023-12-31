from flask import Flask
from flask.cli import FlaskGroup, AppGroup
import click
import os
from app import create_app
# from app.helpers import get_random_datetime, test_hello
app = create_app()

def deploy():
    """Run deployment tasks."""
    from app.extensions import db
    from flask_migrate import upgrade, init, migrate, stamp
    
    app.app_context().push()
    db.create_all()
    # db.init_app(app)
    
    #migrate database to latest revision
    if os.path.exists('migrations') is None:
        init()
        stamp()
        migrate()
        upgrade()
        print('Database initialized.')
    else:
        stamp()
        migrate()
        upgrade()
        print('Database upgraded to latest revision.')
    print('Application deployed.')
    
   
    
# deploy()


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")

@app.cli.command()
def print_date():
    date = get_random_datetime()
    print(date)
    
custom_db = AppGroup("custom_db", help="Custom database commands.")
@custom_db.command("create")
def create_db():
    """Create the database."""
    from app.extensions import db
    db.create_all()
    print('Database created.')
    
app.cli.add_command(custom_db)

if __name__ == '__main__':
    app.run(debug=True)
    # cli()
    # hello()
    # print_date()
    # create_db()
    # deploy()
    # test_hello()
    # print(test_hel
    
    