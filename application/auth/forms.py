from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False

class NewUserForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=2, max=80, message="Virhe! Nimessä tulee olla 2-80 merkkiä!")])
    username = StringField("Username", [validators.Length(min=2, max=25, message="Virhe! Tunnuksessa tulee olla 2-25 merkkiä!")])
    password = PasswordField("Password", [validators.Length(min=4, message="Virhe! Salasanan tulee sisältää vähintään 4 merkkiä!")])

    class Meta:
        csrf = False
