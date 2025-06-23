#Forms were created with the guidance of a 'Learn Flask Login' tutorial and custom vaildation was added using regex (Neupane, 2021)(UIBakery, no date)
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

# WTForm for submitting comments
class CommentForm(FlaskForm):
    content = TextAreaField('Comment', validators=[DataRequired(), Length(
                min=3, max=500)])
    submit = SubmitField('Submit')