from datetime import date
from flask_wtf import Form
from wtforms.fields.core import DateField, StringField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError

class CreateAssessment(Form):
    title = StringField('title', validators=[DataRequired(), Length(max=100)])
    code = StringField('code', validators=[DataRequired(), Length(max=10)])
    deadline = DateField('deadline', format='%d-%m-%Y', validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired(), Length(max=500)])