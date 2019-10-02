from application import db
from application.models import Base

class Item(Base):
    name = db.Column(db.String(144), nullable=False)
    expired = db.Column(db.Boolean, nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    item_category = db.Column(db.Integer, db.ForeignKey('item_category.id'),
                           nullable=False)

    def __init__(self, name):
        self.name = name
        self.expired = False
