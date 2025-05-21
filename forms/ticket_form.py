from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Length, ValidationError, DataRequired

class TicketForm(FlaskForm):
    title = StringField(validators=[DataRequired(),
        Length(max=100, message='Title must be less than 100 characters or less')])
    assignee = SelectField("Assignee", coerce=int, default=0)
    description = TextAreaField(validators=[DataRequired()])
    priority = SelectField(validators=[DataRequired()],
        choices=[('Low'), ('Normal'), ('High'), ('Urgent'), ('Immediate')]) 
    status = SelectField(validators=[DataRequired()],
        choices=[('Open'), ('In Progress'), ('Resolved')]) 

    submit = SubmitField("Submit Ticket")

