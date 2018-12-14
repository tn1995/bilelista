
from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators, PasswordField, StringField
  


class UserTaskForm():

    class Meta:
        csrf = False
    
