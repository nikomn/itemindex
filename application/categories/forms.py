from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators
from application.categories.models import Category

class CategoryForm(FlaskForm):
    name = StringField("Kategorian nimi", [validators.Length(min=2, message="Virhe! Kategorian nimessä tulee olla vähintään 2 merkkiä!")])

    class Meta:
        csrf = False
