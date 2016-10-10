import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nick = db.Column(db.String(32),default="Unnamed player",nullable=False)
    password=db.Column(db.String(32),nullable=False)
    group = db.Column(db.Integer, default=0)
    points= db.Column(db.Integer, default=0)

    def __init__(self,nick="Unnamed player",password="pass",group=0):
        self.nick=nick
        self.password=password
        self.group=group
        self.points=0

    def __repr__(self):
        return self.nick


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    points = db.Column(db.Integer, default=0)

    def __init__(self):
        self.points=0

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship('User',backref=db.backref('user', lazy='dynamic'))
    hightile = db.Column(db.Integer, default=2)
    points = db.Column(db.Integer,default=0)
    start = db.Column(db.DateTime,default=datetime.datetime.utcnow)

    def __init__(self, user):
        self.user=user
