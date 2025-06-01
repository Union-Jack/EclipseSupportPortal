from flask import Flask
from extensions import db, bcrypt, login_manager
from models import user_model

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///EclipseSupportPortal.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'SECRET'

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    from routes.authentication import auth
    from routes.tickets import tickets

    app.register_blueprint(auth)
    app.register_blueprint(tickets)
    
    with app.app_context():
        db.drop_all()
        db.create_all()  
        
    return app

@login_manager.user_loader
def load_user(user_id):
    return user_model.UserModel.query.get(int(user_id))


