from flask import Flask
from extensions import db, bcrypt, login_manager
from models import user_model
from seed_data import seed_database

# Creates and configures the Flask app instance with config, login manager, and blueprints.
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
        #Clears all data so the app and starts it with fresh with the seed data
        #This and the seed data would not be present in a production version however render does not persist sqlite3 db on the free version. 
        db.drop_all()
        db.create_all()  
        seed_database() 
        
    return app

# Tells Flask-Login how to fetch a user from the database.
@login_manager.user_loader
def load_user(user_id):
    with db.session() as session:
        user = session.get(user_model.UserModel, int(user_id)) 

    return user


