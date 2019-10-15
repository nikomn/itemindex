from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators, SelectField
from application.items.models import Item

class ItemForm(FlaskForm):
    name = StringField("Esineen nimi", [validators.Length(min=2, max=120, message="Virhe! Esineen nimessä tulee olla 2-120 merkkiä!")])
    item_category = SelectField('Kategoria', [validators.input_required()], coerce=int)  # message="Virhe! Valitse jokin kategoria!"
    expired = BooleanField("Esine on vanhentunut")

    class Meta:
        csrf = False

class ModifyItemForm(FlaskForm):
    name = StringField("Item name")
    expired = BooleanField("Expired")

    class Meta:
        csrf = False

class ItemSearchForm(FlaskForm):
    item_category = SelectField('Kategoria', [validators.input_required()], coerce=int)

    class Meta:
        csrf = False
