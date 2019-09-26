from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SelectField, validators
from application.items.models import Item
from application.category.models import Category
from flask_login import current_user

class ItemForm(FlaskForm):
    try:
        kategoriat = Category.query.filter_by(account_id=current_user.id)
    except:
        kategoriat = ["Testi"]

    kategoriat = [('cpp', 'C++'), ('py', 'Python')]


    name = StringField("Esineen nimi", [validators.Length(min=2)])
    category = SelectField("Kategoria", choices=kategoriat)


    # name = StringField("Item name", [validators.Length(min=2)], default="Uusi esine")
    expired = BooleanField("Expired")

    class Meta:
        csrf = False

class ModifyItemForm(FlaskForm):
    name = StringField("Item name")
    expired = BooleanField("Expired")

    class Meta:
        csrf = False
