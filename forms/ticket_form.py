from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Length, ValidationError, DataRequired

class TicketForm(FlaskForm):
    title = StringField(validators=[DataRequired(),
        Length(max=100, message='Title must be less than 100 characters or less')])
    description = TextAreaField(validators=[DataRequired()])
    priority = SelectField(validators=[DataRequired()],
        choices=[('Low'), ('Normal'), ('High'), ('Urgent'), ('Immediate')]) 
    submit = SubmitField("Submit Ticket")