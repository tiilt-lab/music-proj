from wtforms import Form, StringField, validators
from math import pi

class InputForm(Form):
    Artist = StringField(
        label='Artist', default="", 
        validators=[validators.InputRequired()])
    Song = StringField(
        label='Song', default="",
        validators=[validators.InputRequired()])