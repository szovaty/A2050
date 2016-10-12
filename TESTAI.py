from socketIO_client import SocketIO, LoggingNamespace
import sys
from time import sleep

myId=1
kmap={"UP":38,"DOWN":40,"LEFT":37,"RIGHT":39}
count=1
def algorithm(data):
    global count
    count+=1
    print(count)
    dir=kmap["UP"]

    socketIO.emit("aiwrite",dir)
    #socketIO.wait(seconds=1)

socketIO = SocketIO('desktop', 5000, LoggingNamespace)

socketIO.on('airead', algorithm)

socketIO.emit("aictl",myId)
socketIO.wait()
