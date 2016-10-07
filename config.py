DIR_UP = (0, -1)
DIR_DOWN = (0, 1)
DIR_RIGHT = (1, 0)
DIR_LEFT = (-1, 0)

keymap={37:DIR_LEFT,38:DIR_UP,39:DIR_RIGHT,40:DIR_DOWN}

secret='o6dkmS7UsiSnNmkS'

def printBoard(board):
    rtv=str()
    for line in board:
        for tile in line:
            rtv+=str(tile)
    return rtv
