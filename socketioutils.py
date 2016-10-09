from flask import session
from app import socketio, gm
from flask_socketio import send,emit,join_room,leave_room
from config import keymap,isLoggedIn
from g2048 import logic
from gm import cGame,printBoard
from db import User

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
        gm.genOutput(uid)
        u=User.query.get(uid)
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
    ev=data["key"]
    uid=session["uid"]
    print("User #"+str(uid)+" issued input:",ev)
    if ev in list(keymap.keys()):
        for game in gm.games:
            if game.uid==uid:
                game.game.shift(keymap[ev])
                gm.genOutput(uid)
                emit("bupdate",printBoard(game),room=room)
                break
