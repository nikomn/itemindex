from application import db
from application.models import Base

item_category = db.Table('item_category',
    db.Column('item_id', db.Integer, db.ForeignKey('item.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'), primary_key=True)
)

class Category(Base):
    name = db.Column(db.String(144), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    item_category = db.Column(db.Integer, db.ForeignKey('item_category.id'),
                           nullable=False)

    def __init__(self, name):
        self.name = name
