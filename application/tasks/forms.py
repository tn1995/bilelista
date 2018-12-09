from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators, DateField

class TaskForm(FlaskForm):
    name = StringField("Bileiden nimi", [validators.Length(min=2, max=30)])
    done = BooleanField("Ovatko bileet jo alkaneet")
    date = DateField("Päivämäärä", format='%d.%m.%Y')
    klo = StringField("Kellonaika")
  
    class Meta:
        csrf = False