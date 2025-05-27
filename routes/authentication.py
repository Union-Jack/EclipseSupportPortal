from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, login_user, logout_user, current_user
from flask_login import LoginManager
from models import user_model
from forms.register_form import RegisterForm
from forms.login_form import LoginForm
from extensions import db, bcrypt
from models.user_model import UserModel
from flask import flash

auth = Blueprint('auth', __name__) 

@auth.route('/')
def home():
        return redirect(url_for('auth.login'))

@auth.route('/login', methods=['GET', 'POST'])
def login():
        form = LoginForm()
        if form.validate_on_submit():
                user = UserModel.query.filter_by(username = form.username.data).first()
                if user:
                        if bcrypt.check_password_hash(user.password, form.password.data):
                                login_user(user)
                                return redirect(url_for('auth.dashboard'))

        return render_template('login.html', form=form)

@auth.route('/register', methods=['GET', 'POST'])
def register():
        form = RegisterForm()

        if form.validate_on_submit():
                hashed_password = bcrypt.generate_password_hash(form.password.data)
                new_user = UserModel(username=form.username.data, password=hashed_password, admin=form.admin.data)
                db.session.add(new_user)
                db.session.commit()
                
                flash("Account created successfully.", "success")

                return redirect(url_for('auth.login'))

        return render_template('register.html', form=form)

@auth.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
        return render_template('dashboard.html') 

@auth.route('/logout', methods=['GET', 'POST'])  
@login_required
def logout():
        return redirect(url_for('auth.login')) 