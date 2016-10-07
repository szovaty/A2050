from app import socketio, g
from flask_socketio import send,emit
from config import printBoard,keymap

@socketio.on('connect')
def conn():
    print("User connected")
    g.new_game()
    emit("bupdate",printBoard(g.board._board))

@socketio.on('disconnect')
def dc():
    print("User disconnected")

@socketio.on('input')
def _input(ev):
    if ev in (37,38,39,40):
        g.shift(keymap[ev])
        emit("bupdate",printBoard(g.board._board))
