from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Length, ValidationError
from models.user_model import UserModel

class RegisterForm(FlaskForm):
        username = StringField(validators=[InputRequired(), Length(
                min=4, max=20)], render_kw={"placeholder": "Username"})       
        password = StringField(validators=[InputRequired(), Length(
                min=4, max=20)], render_kw={"placeholder": "Password"})  
        admin = BooleanField("Admin")
        submit = SubmitField("Register")

        def validate_username(self, username):
                existing_user_username = UserModel.query.filter_by(
                        username=username.data).first()

                if existing_user_username:
                        raise ValidationError(
                                "That username already exists. Please choose a different one.")