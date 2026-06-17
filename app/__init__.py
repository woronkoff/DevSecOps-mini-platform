import os
from flask import Flask
from dotenv import load_dotenv

# Load .env file
load_dotenv()


def create_app():
    app = Flask(__name__)

    # Load configuration from environment
    app.config["APP_NAME"] = os.getenv("APP_NAME")
    app.config["APP_VERSION"] = os.getenv("APP_VERSION")
    app.config["APP_ENV"] = os.getenv("APP_ENV")

    from app.routes import main
    app.register_blueprint(main)
    
    return app