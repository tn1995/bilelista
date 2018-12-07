from application import db
from application.models import Base

class UserTask(Base):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())


    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'),
                           nullable=False)

#@staticmethod
#    def find_osallistujat(done='1'):
 #       stmt = text("SELECT Account.id, Account.name FROM user_task"
  #                   " LEFT JOIN Task ON Task.account_id = Account.id"
   #                  " WHERE (Task.done IS null OR Task.done = :done)"
    #                 " GROUP BY Account.id"
     #                " HAVING COUNT(Task.id) = 0").params(done=done)
      #  res = db.engine.execute(stmt)
#
 #       response = []
  #      for row in res:
   #         response.append({"id":row[0], "name":row[1]})
#
 #       return response