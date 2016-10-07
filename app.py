from flask import Flask
from flask_socketio import SocketIO
from g2048 import logic
from config import *
from flask_wtf.csrf import CsrfProtect


app = Flask(__name__)
app.config['SECRET_KEY'] = secret
socketio = SocketIO(app)
CsrfProtect(app)

g=logic.Game()

import pages
import socketioutils
