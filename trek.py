import cli
from app import create_app
from app.extensions import db

app = create_app()
# Register the custom commands with the application
cli.register(app)

if __name__ == '__main__':
    print(app.url_map)
    