from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Length, ValidationError
from models.user_model import UserModel
import re

class RegisterForm(FlaskForm):
        username = StringField(validators=[InputRequired(), Length(
                min=4, max=20)], render_kw={"placeholder": "Username"})       
        password = StringField(validators=[InputRequired(), Length(
                min=8, max=20)], render_kw={"placeholder": "Password"})  
        admin = BooleanField("Create as Admin")
        submit = SubmitField("Register")

        def validate_username(self, field):
                username = field.data
                existing_user_username = UserModel.query.filter_by(
                        username = username).first()

                if existing_user_username:
                        raise ValidationError(
                                "That username already exists. Please choose a different one.")
                
                if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])[A-Za-z.,\-_]+$', username):
                        raise ValidationError("Username must be at least 4-20 characters long and contain at least one uppercase and one lowercase letter and only '. , - _' characters.")

        def validate_password(self, field):
                password = field.data
                if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[\d\W_]).{8,20}$', password):
                        raise ValidationError("Password must be at least 8-20 characters long and contain at least one uppercase letter, one lowercase letter, and one number or special character.")
