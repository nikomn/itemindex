from application import db
from application.models import Base

class ItemCategory(Base):

    item_id = db.Column(db.Integer, db.ForeignKey('item.id'),
                           nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),
                           nullable=False)

    def __init__(self, name):
        self.name = name
