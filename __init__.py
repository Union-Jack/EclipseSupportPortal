from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from EclipseSupportPortal.models import user_model

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///EclipseSupportPortal.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'SECRET'

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    from EclipseSupportPortal.routes.authentication import auth
    from EclipseSupportPortal.routes.tickets import tickets

    app.register_blueprint(auth)
    app.register_blueprint(tickets)
    
    return app

@login_manager.user_loader
def load_user(user_id):
    return user_model.UserModel.query.get(int(user_id))


