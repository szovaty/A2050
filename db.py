from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nick = db.Column(db.String(32),default="Unnamed player")
    password=db.Column(db.String(32),nullable=False)
    group = db.Column(db.Integer, default=0)
    points= db.Column(db.Integer, default=0)

    def __init__(self,nick,email,group=0):
        self.email = email
        self.group=group
        self.points=0


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
    end=db.Column(db.Boolean,default=False)
    board=db.Column(db.String(16),nullable=False)

    def __init__(self, user, board):
        self.user=user
        self.board=board
