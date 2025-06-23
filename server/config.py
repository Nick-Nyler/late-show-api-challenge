
import os

class Config:
    """
    Configuration class for the Flask application.
    Defines database URI, JWT secret key, and other settings.
    """
    
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:0722231200@localhost:5432/late_show_db"
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "super-secret-jwt-key-replace-me-in-prod")