# app/__init__.py
from flask import Flask
from app.routes import routes  # Import the Blueprint from routes.py

def create_app():
    app = Flask(__name__)
    app.register_blueprint(routes)  # Register the Blueprint
    return app
