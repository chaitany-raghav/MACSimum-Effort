import socket
from _thread import *
import sys
import Config
from Player import Player
import pickle

#The ip of the server
server = Config.ServerIP
port = Config.ServerPort

currentPlayer = 0

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    s.bind((server,port))
except socket.error as e:
    print(e)
 
s.listen(Config.maxPlayerCount)
print("Wating for a connection,Server Started")


pos=[
    Player(Config.PlayerOffSet,(Config.WindowHeight-Config.PlayerLength)/2,Config.PlayerWidth,Config.PlayerLength,0,(255,0,0)),
    Player(Config.WindowWidth-Config.PlayerWidth-Config.PlayerOffSet,(Config.WindowHeight-Config.PlayerLength)/2,Config.PlayerWidth,Config.PlayerLength,1,(0,255,0)),
    Player((Config.WindowWidth-Config.PlayerLength)/2,Config.PlayerOffSet,Config.PlayerLength,Config.PlayerWidth,2,(0,0,255)),
    Player((Config.WindowWidth-Config.PlayerLength)/2,Config.WindowHeight-Config.PlayerWidth-Config.PlayerOffSet,Config.PlayerLength,Config.PlayerWidth,3,(128,128,0))
    ]

def threaded_client(conn,Player):
    conn.send(pickle.dumps(pos[Player]))
    while True:
        try:
            data=pickle.loads(conn.recv(2048))
            pos[Player]=data
            if not data:
                print("Disconnected")
                break
            else:
                reply=pickle.dumps(pos)
                print("Recived:",data)
                print("Sending:",reply) 

            conn.sendall(reply)
        except:
            break
    global currentPlayer
    currentPlayer-=1
    print("Lost connection")
    conn.close()


while True:
    conn,addr=s.accept()
    print("Connecting to:",addr)
    start_new_thread(threaded_client,(conn,currentPlayer))
    currentPlayer+=1