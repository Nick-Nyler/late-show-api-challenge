from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from server.config import Config

from server.models import db, User, Guest, Episode, Appearance

from server.controllers.auth_controller import auth_bp
from server.controllers.guest_controller import guest_bp
from server.controllers.episode_controller import episode_bp
from server.controllers.appearance_controller import appearance_bp

def create_app():
    """
    Factory function to create and configure the Flask application.
    This pattern is useful for testing and handling different environments.
    """
    app = Flask(__name__)
    
    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db) 
    JWTManager(app)

    app.register_blueprint(auth_bp, url_prefix='/')
    app.register_blueprint(guest_bp, url_prefix='/')
    app.register_blueprint(episode_bp, url_prefix='/')
    app.register_blueprint(appearance_bp, url_prefix='/')

    @app.route('/')
    def index():
        return "Welcome to the Late Show API!"

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

