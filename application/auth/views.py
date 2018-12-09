from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, SignupForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    
    if not user:
        return render_template("auth/loginform.html", form = form,
                                error = "No such username or password")


    login_user(user)
    return redirect(url_for("index"))   
#
@app.route("/auth/signup", methods = ["GET", "POST"])
def auth_signup():
    if request.method == "GET":
        return render_template("auth/signupform.html", form = SignupForm())

    form = SignupForm(request.form)
    # mahdolliset validoinnit
    
    user = User.query.filter_by(username=form.username.data).first()

    if len(form.username.data) < 3:
        return render_template("auth/signupform.html", form = form,
                                error = "Käyttäjätunnuksen tulee olla vähintää 3 merkkiä ja enintään 20 merkkiä")

    if len(form.username.data) > 20:
        return render_template("auth/signupform.html", form = form,
                                error = "Käyttäjätunnuksen tulee olla vähintää 3 merkkiä ja enintään 20 merkkiä")
    if len(form.name.data) < 1:
        return render_template("auth/signupform.html", form = form,
                                error = "Et laittanut nimeäsi")


    if user:
        return render_template("auth/signupform.html", form = form,
                                error = "Käyttäjä on jo olemassa")
    if form.password.data != form.repeatpassword.data:
        return render_template("auth/signupform.html", form = form,
                                error = "Salasanat eivät täsmää")

    if len(form.password.data) < 3:
        return render_template("auth/signupform.html", form = form,
                                error = "Salasanan tulee olla vähintää 3 merkkiä ja enintään 20 merkkiä")
    
    if len(form.password.data) > 20:
        return render_template("auth/signupform.html", form = form,
                                error = "Salasanan tulee olla vähintää 3 merkkiä ja enintään 20 merkkiä")

    account = User(form.name.data)
    account.username = form.username.data
    account.password = form.password.data
  
    db.session().add(account)
    db.session().commit()
    return redirect(url_for("index"))   

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))    

