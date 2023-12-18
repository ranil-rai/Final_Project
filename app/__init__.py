from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .config import Config
from .routes import main as main_blueprint
from .extensions import db
from .extensions import login_manager

# db = SQLAlchemy()
# login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def create_app(config_class=Config):
    app = Flask(__name__)
    app.register_blueprint(main_blueprint, url_prefix='/')
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    from .routes import main as main_routes
    app.register_blueprint(main_routes, name='unique_main')

    # If you have other blueprints, you can register them here
    # from .some_module import some_blueprint
    # app.register_blueprint(some_blueprint)

    return app
