from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application import app, db, login_required
from application.tasks.models import Task
from application.tasks.forms import TaskForm

from application.authtasks.models import UserTask

from application.auth.models import User
from application.auth.forms import LoginForm, SignupForm


@app.route("/tasks/", methods=["GET"])
def tasks_index():
    return render_template("tasks/list.html", tasks = Task.find_lista())

#creates new   
@app.route("/tasks/new/")
@login_required()
def tasks_form():
    return render_template("tasks/new.html", form = TaskForm())

#sets tasks done  
@app.route("/tasks/<task_id>/", methods=["POST"])
@login_required()
def tasks_set_done(task_id):

    t = Task.query.get(task_id)
    if t.account_id != current_user.id:
        return redirect(url_for("tasks_index"))
    if t.done == False:
        t.done = True
        db.session().commit()
        return redirect(url_for("tasks_index"))

    if t.done == True:
        t.done = False
    db.session().commit()

  
    return redirect(url_for("tasks_index"))
#deletes tasks
@app.route("/tasks/delete/<task_id>/", methods=["POST"])
@login_required()
def tasks_delete(task_id):

    t = Task.query.get(task_id)

    if t.account_id != current_user.id:
        return redirect(url_for("tasks_index"))
    UserTask.delete_participator_for_deleted_task(task_id)
    db.session().delete(t)
    db.session().commit()
    
  
    return redirect(url_for("tasks_index"))

#creates tasks  
@app.route("/tasks/", methods=["POST"])
@login_required()
def tasks_create():
    form = TaskForm(request.form)
    
    if not form.validate():
        return render_template("tasks/new.html", form = form)
    
    t = Task(form.name.data, form.done.data, form.date.data, form.klo.data, form.location.data)

    t.account_id = current_user.id
    
  
    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("tasks_index"))

