from flask import session
from app import socketio, gm, db
from flask_socketio import send,emit,join_room,leave_room
from config import keymap,isLoggedIn
from g2048 import logic
from gm import cGame,printBoard
from db import User,Game,getSessionScores

room="game"

@socketio.on('connect')
def conn():
    if isLoggedIn():
        uid=session["uid"]
        join_room(room)
        ng=gm.hasGameWithId(uid)
        if ng==None:
            ng=cGame(logic.Game(),uid)
            ng.game.new_game()
            gm.addTable(ng)
        u=User.query.get(uid)
        g=Game(u)
        db.session.add(g)
        db.session.commit()
        emit("player_connect",(uid,u.nick),room=room)
        emit("bupdate",printBoard(ng))
        print("User #"+str(uid)+" connected")
        emit("load_others",gm.getGames(uid))

@socketio.on('disconnect')
def dc():
    if isLoggedIn():
        uid=session["uid"]
        emit("player_disconnect",uid,room=room)

        gm.removeTable(uid)
        leave_room(room)
        print("User #"+str(uid)+" disconnected")

@socketio.on('input')
def _input(data):
    if not isLoggedIn():
        return
    ev=data["key"]
    uid=session["uid"]
    print("User #"+str(uid)+" issued input:",ev)
    if ev in list(keymap.keys()):
        gm.shift(uid,ev)
        if gm.gameOver(uid):
            u=User.query.get(uid)
            g=Game.query.filter_by(user=u).order_by(db.desc(Game.start)).first()
            g.hightile=gm.getHightile(uid)
            g.points=gm.getPoints(uid)
            db.session.commit()
        emit("bupdate",printBoard(gm.get(uid)),room=room)
        emit("score_update",getSessionScores(),room=room)

@socketio.on("aictl")
def _aictl(id):
    game=gm.hasGameWithId(id)
    if game==None:
        return
    session["uid"]=id
    emit("airead",printBoard(game,includeid=False))

@socketio.on("aiwrite")
def _aiwrite(dir):
    if isLoggedIn():
        print(dir)
        if dir in list(keymap.keys()):
            gm.shift(session["uid"],dir)
            back=printBoard(gm.hasGameWithId(session["uid"]),includeid=False)
            emit("airead",back)
            emit("bupdate",str(session["uid"])+" "+back,room=room)
