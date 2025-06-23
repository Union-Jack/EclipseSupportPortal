#Routes were implemented following the Flask-Login documentation and a 'Learn Flask Login' tutorial (Flask-Login, no date)(Neupane, 2021).
from flask import Blueprint, render_template, redirect, url_for, session
from flask_login import login_required, login_user, logout_user, current_user
from flask_login import LoginManager
from models import user_model
from forms.register_form import RegisterForm
from forms.login_form import LoginForm
from extensions import db, bcrypt
from models.user_model import UserModel
from flask import flash

#Blueprint for grouping authenitcation related routes and logic
auth = Blueprint('auth', __name__) 

#Default route redirecting users to the login page when accessing the root URL.
@auth.route('/')
def home():
        return redirect(url_for('auth.login'))

#Route for the login page
@auth.route('/login', methods=['GET', 'POST'])
def login():
        form = LoginForm()

        #If the username and password could be valid attempt to log in 
        if form.validate_on_submit():
                user = UserModel.query.filter_by(username = form.username.data).first()
                #If the user exists and the username and password match, login
                if user and bcrypt.check_password_hash(user.password, form.password.data):
                        login_user(user)
                        return redirect(url_for('tickets.homepage'))
                #If the user does not exist or the username and password are incorrect present validation error
                else:
                        flash("Incorrect username or password. Please try again.", "danger") 


        return render_template('login.html', form=form)

#Route for the register page
@auth.route('/register', methods=['GET', 'POST'])
def register():
        form = RegisterForm()

        #Commits user to database if the username and password are vallid and redirects to the login page
        if form.validate_on_submit():
                hashed_password = bcrypt.generate_password_hash(form.password.data)
                new_user = UserModel(username=form.username.data, password=hashed_password, admin=form.admin.data)              
                db.session.add(new_user)             
                db.session.commit()
                
                flash("Account created successfully.", "success")

                return redirect(url_for('auth.login'))
        
        #Validates input errors
        for field, errors in form.errors.items():
                for error in errors:
                        flash(f"{field.capitalize()}: {error}", "danger")  


        return render_template('register.html', form=form)

#Route for loging out of the application
@auth.route('/logout', methods=['GET', 'POST'])  
@login_required
def logout():
        #Clears the session data and ridirects the user to the login page
        session.clear()
        return redirect(url_for('auth.login')) 