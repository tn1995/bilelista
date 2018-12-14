from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators, DateField

class TaskForm(FlaskForm):
    name = StringField("Bileiden nimi", [validators.Length(min=2, max=30)])
    done = BooleanField("Ovatko bileet jo alkaneet")
    date = DateField("Pvm", format='%Y-%m-%d')
    klo = StringField("Klo", [validators.Length(min=1, max=10)])
    location = StringField("Sijainti", [validators.Length(min=2, max=30)])
  
    class Meta:
        csrf = False