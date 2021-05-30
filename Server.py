from Ball import Ball
import socket
from _thread import *
import Config
from Player import Player
import pickle
import pygame as pg
from Ball import Ball

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
    Player(Config.PlayerOffSet-Config.PlayerWidth,(Config.WindowHeight-Config.PlayerLength)/2,Config.PlayerWidth,Config.PlayerLength,0,False,(255,0,0)),
    Player(Config.WindowWidth-Config.PlayerOffSet,(Config.WindowHeight-Config.PlayerLength)/2,Config.PlayerWidth,Config.PlayerLength,1,False,(0,255,0)),
    Player((Config.WindowWidth-Config.PlayerLength)/2,Config.PlayerOffSet-Config.PlayerWidth,Config.PlayerLength,Config.PlayerWidth,2,False,(0,0,255)),
    Player((Config.WindowWidth-Config.PlayerLength)/2,Config.WindowHeight-Config.PlayerOffSet,Config.PlayerLength,Config.PlayerWidth,3,False,(128,128,0))
    ]
ball=Ball(Config.WindowWidth/2,Config.WindowHeight/2,Config.BallRadius,Config.BallSpeed,(20,60,99))

def ball_mover(p,b):
    clock=pg.time.Clock()
    while True:
        clock.tick(Config.FPS)
        b.move(p)

def threaded_client(conn,Player):
    pos[Player].isActive=True
    conn.send(pickle.dumps(pos[Player]))
    while True:
        try:
            #ball.move()
            data=pickle.loads(conn.recv(2048))
            pos[Player]=data
            if not data:
                print("Disconnected")
                break
            else:
                temp=[]
                temp.append(pos)
                temp.append(ball)
                reply=pickle.dumps(temp)
                #print("Recived:",data)
                #print("Sending:",reply) 

            conn.sendall(reply)
        except:
            break

    global currentPlayer
    pos[Player].isActive=False
    currentPlayer-=1
    print("Lost connection")
    conn.close()

start_new_thread(ball_mover,(pos,ball))

while True:
    conn,addr=s.accept()
    print("Connecting to:",addr)
    #start_new_thread(threaded_client,(conn,currentPlayer))
    #currentPlayer+=1
    
    for p in pos:
        if not p.isActive:
            start_new_thread(threaded_client,(conn,p.id))
            currentPlayer+=1
            break
    
