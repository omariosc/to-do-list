from flask_wtf import Form
from wtforms.fields.core import DateField, StringField
from wtforms.validators import DataRequired

class CreateAssessment(Form):
    title = StringField('title', validators=[DataRequired()])
    code = StringField('code', validators=[DataRequired()])
    deadline = StringField('deadline', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])