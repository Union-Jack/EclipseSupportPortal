#Forms were created with the guidance of a 'Learn Flask Login' tutorial and custom vaildation was added using regex (Neupane, 2021)(UIBakery, no date)
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError

# WTForm for authenticating users
class LoginForm(FlaskForm):
        username = StringField(validators=[InputRequired(), Length(
                min=4, max=20)], render_kw={"placeholder": "Username"})       
        password = StringField(validators=[InputRequired(), Length(
                min=4, max=20)], render_kw={"placeholder": "Password"})  

        submit = SubmitField("Login")