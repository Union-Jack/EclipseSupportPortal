from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Length, ValidationError, DataRequired
import re

class TicketForm(FlaskForm):
    title = StringField(validators=[DataRequired(),
        Length(min=3, max=100)])
    assignee = SelectField("Assignee", coerce=int, default=0)
    description = TextAreaField(validators=[DataRequired(),
        Length(min=3, max=1000)])
    priority = SelectField(validators=[DataRequired()],
        choices=[('Low'), ('Normal'), ('High'), ('Urgent'), ('Immediate')]) 
    status = SelectField(validators=[DataRequired()],
        choices=[('Open'), ('In Progress'), ('Resolved')]) 

    submit = SubmitField("Submit Ticket")

    def validate_title(self, field):
        if not re.match(r'^(?=.*[A-Za-z])[A-Za-z\s]+$', field.data):  
            raise ValidationError("Title must contain at least one letter and can only include letters and spaces.")

