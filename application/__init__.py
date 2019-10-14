from flask import Flask
from config import Config


def create_app():
    """Construct the core application."""

    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        from .main import main_routes
        app.register_blueprint(main_routes.main_bp)
        return app
