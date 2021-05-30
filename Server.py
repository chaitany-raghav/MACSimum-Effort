import pygame as pg

import socket
from _thread import *
import pickle

import Config
from Player import Player
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
    Player(Config.PlayerOffSet-Config.PlayerWidth,(Config.WindowHeight-100-Config.PlayerLength)/2,Config.PlayerWidth,Config.PlayerLength,0,False,(255,0,0)),
    Player(Config.WindowWidth-Config.PlayerOffSet,(Config.WindowHeight-100-Config.PlayerLength)/2,Config.PlayerWidth,Config.PlayerLength,1,False,(0,255,0)),
    Player((Config.WindowWidth-Config.PlayerLength)/2,Config.PlayerOffSet-Config.PlayerWidth,Config.PlayerLength,Config.PlayerWidth,2,False,(0,0,255)),
    Player((Config.WindowWidth-Config.PlayerLength)/2,Config.WindowHeight-100-Config.PlayerOffSet,Config.PlayerLength,Config.PlayerWidth,3,False,(128,128,0))
    ]
ball=Ball(Config.WindowWidth/2,(Config.WindowHeight-100)/2,Config.BallRadius,Config.BallSpeed,(20,60,99))
score=["----","----","----","----"]
music=[]
def ball_mover(p,b,s,m):
    clock=pg.time.Clock()
    while True:
        clock.tick(Config.FPS)
        m.clear()
        b.move(p,s,m)

def threaded_client(conn,Player):
    pos[Player].isActive=True
    score[Player]=0
    conn.send(pickle.dumps(pos[Player]))
    while True:
        temp2=music.copy()
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
                temp.append(score)
                temp.append(temp2)
                reply=pickle.dumps(temp)
                #print("Recived:",data)
                #print("Sending:",reply) 
                #print(score)
            conn.sendall(reply)
        except:
            break

    global currentPlayer
    pos[Player].isActive=False
    score[Player]="----"
    currentPlayer-=1
    print("Lost connection")
    conn.close()

start_new_thread(ball_mover,(pos,ball,score,music))

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
    
