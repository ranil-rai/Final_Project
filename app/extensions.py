# app/extensions.py

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
db = SQLAlchemy()

# Add other extensions like Flask-Login here
login_manager = LoginManager()
