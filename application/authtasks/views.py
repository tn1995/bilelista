from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application import app, db, login_required
from application.authtasks.models import UserTask
from application.auth.forms import LoginForm, SignupForm
from application.tasks.models import Task
from application.tasks.forms import TaskForm
from application.auth.models import User





@app.route("/information/", methods=["GET"])
@login_required
def information_index():
    return render_template("authtasks/party.html") 

 #shows the information of the party 
@app.route("/information/<task_id>")
@login_required()
def tasks_information(task_id):
    t = Task.query.get(task_id)

    return render_template("authtasks/party.html", party = t, tasks_participators=UserTask.find_tasks_participators(task_id))

#take part in party  
@app.route("/information/osallistu/<task_id>", methods=["POST"])
@login_required()
def tasks_participate(task_id):
    t=UserTask(current_user.id, task_id)
    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("tasks_information", task_id=task_id))

#delete participation
@app.route("/information/delete/<task_id>/", methods=["POST"])
@login_required()
def participation_delete(task_id):
    
    UserTask.delete_participator(current_user.id, task_id)
    return redirect(url_for("tasks_information", task_id=task_id))

#shows user info
@app.route("/information/user/<username>")
@login_required()
def user_information(username):
  
    return render_template("authtasks/user.html", user_information=User.find_users_by_username(username), users_tasks=Task.find_users_tasks(username))



