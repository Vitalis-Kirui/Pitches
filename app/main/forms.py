from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,TextAreaField,SubmitField
from wtforms.validators import Required

class PitchesForm(FlaskForm):

    pitch_title = StringField('Pitch title',validators=[Required()])
    pitch_category = SelectField('Category',
                                 choices=[('Select category',
                                           'Select category'),
                                          ('interview', 'Interview'),
                                          ('discussion', 'Discussion'),
                                          ('promotion', 'Promotion'),
                                          ('friendship', 'Friendship')],
                                 validators=[Required()])
    pitch_itself= TextAreaField('Enter pitch', validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')