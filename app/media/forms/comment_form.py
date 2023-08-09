from flask_wtf import FlaskForm
from wtforms import SelectField, StringField
from wtforms.validators import DataRequired


class CommentForm(FlaskForm):
    rating = SelectField('Rating', choices=[(str(i), str(i)) for i in range(1, 11)])
    text = StringField('Comment', render_kw={'rows': 5, 'cols': 50}, validators=[DataRequired()])