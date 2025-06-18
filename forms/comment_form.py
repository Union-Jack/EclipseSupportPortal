from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class CommentForm(FlaskForm):
    content = TextAreaField('Comment', validators=[DataRequired(), Length(
                min=3, max=500)])
    submit = SubmitField('Submit')