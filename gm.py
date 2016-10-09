from os import remove
def printBoard(game,includeid=True):
    if includeid:
        rtv=str(game.uid)
        rtv+=" "+str(game.game.score)
    else:
        rtv=str(game.game.score)
    for line in game.game.board._board:
        for tile in line:
            rtv+=" "+str(tile)
    return rtv

outputFolder="files/"

class cGame:
    def __init__(self,game,uid):
        self.game=game
        self.uid=uid

class GameManager:
    def __init__(self):
        self.games=list()

    def addTable(self,game):
        self.games.append(game)

    def removeTable(self,uid):
        for x,game in enumerate(self.games):
            if game.uid==uid:
                remove(outputFolder+"out"+str(uid))
                del self.games[x]

    def hasGameWithId(self,id):
        for game in self.games:
            if game.uid==id:
                return game
        return None

    def getGames(self,id):
        rtv=list()
        for game in self.games:
            if game.uid!=id:
                rtv.append(printBoard(game))
        return rtv

    def genOutput(self,id):
        for game in self.games:
            if game.uid==id:
                with open(outputFolder+"out"+str(id),"w") as f:
                    f.write(printBoard(game,includeid=False))
