from flask_wtf import FlaskForm
from wtforms import SelectField, StringField
from wtforms.validators import DataRequired


class ReviewForm(FlaskForm):
    rating = SelectField('Rating', choices=[(str(i), str(i)) for i in range(1, 11)])
    title = StringField('Title', validators=[DataRequired()])
    text = StringField('Text')
    
