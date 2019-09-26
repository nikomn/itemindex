from application import db
from application.models import Base

class ItemCategory(Base):
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),
                           nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'),
                           nullable=False)

    # def __init__(self, name):
    #     self.name = name
