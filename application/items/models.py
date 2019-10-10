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

    @staticmethod
    def get_items_in_category(category_id):
        pass
        stmt = text("SELECT Item.name FROM item "
                    "LEFT JOIN Account ON Item.account_id=Account.id"
                    "LEFT JOIN Category ON Category.account_id=Account.id"
                    "WHERE Category.id = :category_id").params(category_id=category_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append(row)

        return response

    @staticmethod
    def get_expired_items(expired_status=True):
        pass
        stmt = text("SELECT Item.name FROM item "
                    "LEFT JOIN Account ON Item.account_id=Account.id"
                    "LEFT JOIN Category ON Category.account_id=Account.id"
                    "WHERE Item.expired = :expired_status").params(expired_status=expired_status)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append(row)

        return response

    @staticmethod
    def get_nonexpired_items(expired_status=False):
        pass
        stmt = text("SELECT Item.name FROM item "
                    "LEFT JOIN Account ON Item.account_id=Account.id"
                    "LEFT JOIN Category ON Category.account_id=Account.id"
                    "WHERE Item.expired = :expired_status").params(expired_status=expired_status)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append(row)

        return response
