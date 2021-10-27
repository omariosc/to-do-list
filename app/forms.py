from flask_wtf import Form
from wtforms.fields.core import StringField
from wtforms.fields.html5 import DateField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired, Length

class CreateAssessment(Form):
    title = StringField('title', validators=[DataRequired(), Length(max=100)])
    code = StringField('code', validators=[DataRequired(), Length(max=10)])
    deadline = DateField('deadline')
    description = TextAreaField('description', validators=[DataRequired(), Length(max=500)])
