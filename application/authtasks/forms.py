
from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators, PasswordField, StringField
  


class Osallistuminen():
    done = BooleanField("Done")
