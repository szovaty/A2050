import g2048.logic.Game as gGame

class cGame:
    def __init__(self,game,tableid):
        self.game=game
        self.tableid=tableid

class GameManager:
    def __init__(self):
        self.games=list()

    def addTable(self,game):
        self.games.append(game)

    def removeTable(self,game):
