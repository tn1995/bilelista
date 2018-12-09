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
    def find_tasks_osallistujat(task_id):
        stmt = text("SELECT Account.name FROM Account"
                    " LEFT JOIN User_task ON User_task.account_id = Account.id"
                    " WHERE (User_task.account_id = Account.id)"
                    " AND User_task.task_id = :task_id"
                    " GROUP BY Account.id").params(task_id=task_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0]})
        return response
    @staticmethod
    def delete_osallistuja(account_id, task_id):
        stmt = text("DELETE FROM user_task"
                    " WHERE User_task.account_id = account_id"
                    " AND User_task.task_id = task_id").params(account_id=account_id, task_id=task_id)
        res = db.engine.execute(stmt)

        #response = []
        #for row in res:
        #    response.append({"name":row[0]})
        return res

    def __init__(self, account_id, task_id):
        self.account_id = account_id
        self.task_id = task_id

