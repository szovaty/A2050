from flask import render_template,request,session,redirect,url_for
from db import User
from forms import LoginForm
from app import app,db

@app.route('/',methods=("GET","POST"))
def login():
    if "uid" in list(session.keys()):
        return redirect(url_for("index"))
    form=LoginForm(request.form)
    if form.validate_on_submit():
        user=User.query.filter_by(nick=form.nick.data).first()
        if user!= None:
            if user.password==form.password.data:
                session["uid"]=user.id
                return redirect(url_for("index"))
        else:
            return "Auth problem"
    return render_template("login.html",form=form)

@app.route('/game/')
def index():
    if "uid" in list(session.keys()):
        return render_template("index.html")
    else:
        return redirect(url_for("login"))

@app.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route('/files/out<name>')
def out(name):
    u=User.query.filter_by(nick=name).first()
    if u!=None and u.group>1:
        with open("files/out"+str(u.id)) as f:
            return f.readline()
    else:
        return "Somehting went wrong."
