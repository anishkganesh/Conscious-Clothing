from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
# note: pip install wtforms[email] must be done separately if done on new system
from wtforms.validators import DataRequired

# Clothing Form
class ClothingForm(FlaskForm):
    link = TextAreaField('Paste Link Here:', validators=[DataRequired()])
    submit = SubmitField('Submit')
    chat = StringField('Chat')
