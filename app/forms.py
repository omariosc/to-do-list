import datetime
from flask_wtf import Form
from wtforms.fields.core import DateField, StringField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired, Length

class CreateAssessment(Form):
    title = StringField('title', validators=[DataRequired(), Length(max=100)])
    code = StringField('code', validators=[DataRequired(), Length(max=10)])
    deadline = StringField('deadline', validators=[DataRequired(), Length(max=10)])
    description = TextAreaField('description', validators=[DataRequired(), Length(max=500)])