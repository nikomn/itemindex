from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators, SelectField
from application.items.models import Item

class ItemForm(FlaskForm):
    name = StringField("Item name", [validators.Length(min=2)])
    # name = StringField("Item name", [validators.Length(min=2)], default="Uusi esine")
    item_category = SelectField('Kategoria', [validators.input_required()], coerce=int)
    expired = BooleanField("Expired")

    class Meta:
        csrf = False

class ModifyItemForm(FlaskForm):
    name = StringField("Item name")
    expired = BooleanField("Expired")

    class Meta:
        csrf = False
