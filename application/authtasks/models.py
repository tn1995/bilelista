from application import db
from application.models import Base
from sqlalchemy.sql import text

class UserTask(Base):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())


    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'),
                           nullable=False)

    @staticmethod
    def find_tasks_osallistujat():
        stmt = text("SELECT Account.name FROM Account"
                     " LEFT JOIN User_task ON User_task.account_id = Account.id"
                     " WHERE (User_task.account_id = Account.id)"
                     " GROUP BY Account.id")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})
        return response