from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Käyttäjänimi")
    password = PasswordField("Salasana")
  
    class Meta:
        csrf = False

class SignupForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=2, max=10)])
    username = StringField("Käyttäjänimi", [validators.Length(min=2, max=10)])
    password = PasswordField("Salasana",  [validators.Length(min=2, max=10)])
    repeatpassword = PasswordField("Salasana uudestaan", [validators.Length(min=2, max=10)])
  
    class Meta:
        csrf = False
