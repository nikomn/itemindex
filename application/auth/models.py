from application import db
from application.models import Base
from application.categories.models import Category

from sqlalchemy.sql import text



class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    items = db.relationship("Item", backref='account', lazy=True)
    categorys = db.relationship("Category", backref='account', lazy=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    # @staticmethod
    # def find_users_with_no_items():
    #     stmt = text("SELECT Account.id, Account.name FROM Account"
    #                  " LEFT JOIN Item ON Item.account_id = Account.id"
    #                  " WHERE (Item.expired IS null OR Item.expired = 1)"
    #                  " GROUP BY Account.id"
    #                  " HAVING COUNT(Item.id) = 0")
    #     res = db.engine.execute(stmt)
    #
    #     response = []
    #     for row in res:
    #         response.append({"id":row[0], "name":row[1]})
    #
    #     return response


    @staticmethod
    # def find_users_with_no_items(expired=True):
    def find_users_with_no_items(expired=True):
        stmt = text("SELECT Account.id, Account.name FROM Account"
                     " LEFT JOIN Item ON Item.account_id = Account.id"
                     # " WHERE (Item.expired IS null OR Item.expired = :done)"
                     " WHERE (Item.expired IS null OR Item.expired IS :done)"
                     " GROUP BY Account.id"
                     " HAVING COUNT(Item.id) = 0").params(done=expired)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        return response
