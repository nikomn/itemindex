from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators
from application.categories.models import Category

class CategoryForm(FlaskForm):
    name = StringField("Kategorian nimi", [validators.Length(min=2)])

    class Meta:
        csrf = False
