from flask import render_template,request,session,redirect,url_for
from app import app
from forms import LoginForm
from db import db,User
import hashlib

@app.route('/',methods=("GET","POST"))
def login():
    form=LoginForm(request.form)
    if form.validate_on_submit():
        user=User.query.filter_by(nick=form.nick.data).first()
        print(1)
        if user!= None:
            print(2)
            if user.password==form.password.data:
                print(3)
                session["uid"]=user.id
                return redirect(url_for("index"))
        else:
            return "Auth problem"
    return render_template("login.html",form=form)

@app.route('/game/')
def index():
    if "uid" in list(session.keys()):
        return render_template("index.html",size=4,num=2)
    else:
        return redirect(url_for("login"))

@app.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for("login"))
