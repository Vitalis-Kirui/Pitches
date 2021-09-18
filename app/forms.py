from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class PitchesForm(FlaskForm):

    title = StringField('Pitch title',validators=[Required()])
    pitch = TextAreaField('Enter pitch', validators=[Required()])
    submit = SubmitField('Submit')