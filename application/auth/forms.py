from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False

class SignupForm(FlaskForm):
    name = StringField("name", [validators.Length(min=2, max=10)])
    username = StringField("Username", [validators.Length(min=2, max=10)])
    password = PasswordField("Password",  [validators.Length(min=2, max=10)])
    repeatpassword = PasswordField("Password", [validators.Length(min=2, max=10)])
  
    class Meta:
        csrf = False
