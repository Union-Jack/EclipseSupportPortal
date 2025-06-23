#Forms were created with the guidance of a 'Learn Flask Login' tutorial and custom vaildation was added using regex (Neupane, 2021)(UIBakery, no date)
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Length, ValidationError, DataRequired
import re

# WTForm for creating and editing tickets and validating tickets
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
            raise ValidationError("Title must contain at least three letters and can only include letters and spaces.")

