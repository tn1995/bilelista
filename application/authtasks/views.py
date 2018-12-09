from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application import app, db, login_required
from application.authtasks.models import UserTask
from application.auth.forms import LoginForm, SignupForm
from application.tasks.models import Task
from application.tasks.forms import TaskForm



@app.route("/information/", methods=["GET"])
@login_required
def information_index():
    return render_template("authtasks/bile.html") 

 #shows the information of the party 
@app.route("/information/<task_id>")
@login_required()
def tasks_information(task_id):
    t = Task.query.get(task_id)

    return render_template("authtasks/bile.html", bile = t, tasks_osallistujat=UserTask.find_tasks_osallistujat(task_id))


#take part in party  
@app.route("/information/osallistu/<task_id>", methods=["POST"])
@login_required()
def tasks_osallistu(task_id):
    t=UserTask(current_user.id, task_id)
    
  
    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("tasks_information", task_id=task_id))

#delete osallistu
@app.route("/information/delete/<task_id>/", methods=["POST"])
@login_required()
def osallistuminen_delete(task_id):
    
    UserTask.delete_osallistuja(current_user.id, task_id)
    return redirect(url_for("tasks_information", task_id=task_id))

