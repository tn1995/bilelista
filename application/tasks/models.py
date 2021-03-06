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
    date = db.Column(db.String, nullable=False)
    klo = db.Column(db.String, nullable=False)
    location = db.Column(db.String(144), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, name, done, date, klo, location):
        self.name = name
        self.done = False
        self.date = date
        self.klo = klo
        self.location = location

    #Show all partys
    @staticmethod
    def find_lista():
        stmt = text("SELECT Account.username AS account_username, Task.id, Task.done, Task.name, Task.date, Task.klo, Task.location FROM Account"
                     " LEFT JOIN Task ON Task.account_id = Account.id"
                     " WHERE (Task.account_id = Account.id)"
                     " GROUP BY Task.id, account.username")
        res = db.engine.execute(stmt)

        return res
    #Shows chosen users partys
    @staticmethod
    def find_users_tasks(username):
        stmt = text("SELECT Task.id, Task.name, Task.date FROM Account"
                     " JOIN Task ON Account.id = Task.account_id"
                     " WHERE (Account.username = :username)"
                     " GROUP BY Account.id, task.name, task.id").params(username=username)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "date":row[2]})

        return response
        