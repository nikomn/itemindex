from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators

class ItemForm(FlaskForm):
    name = StringField("Item name", [validators.Length(min=2)])
    expired = BooleanField("Expired")
 
    class Meta:
        csrf = False
