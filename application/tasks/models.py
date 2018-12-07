from application import db
from application.models import Base
from sqlalchemy.sql import text

class Task(Base):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    done = db.Column(db.Boolean, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, name):
        self.name = name
        self.done = False


    @staticmethod
    def find_lista():
        stmt = text("SELECT Account.name AS account_name, Task.id, Task.done, Task.name FROM Account"
                     " LEFT JOIN Task ON Task.account_id = Account.id"
                     " WHERE (Task.account_id = Account.id)"
                     " GROUP BY Task.id")
        res = db.engine.execute(stmt)

#        response = []
#        for row in res:
#            response.append({"name":row[1]})

        return res