import socket
from _thread import *
import sys

#The ip of the server
server = "10.0.0.2"
port = 5555

maxPlayerCount=2

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    s.bind((server,port))
except socket.error as e:
    print(e)
 
s.listen(maxPlayerCount)
print("Wating for a connection,Server Started")

def read_pos(str):
    str =str.split(',')
    return int(str[0]),int(str[1])

def make_pos(tup):
    return str(tup[0])+","+str(tup[1])

pos=[(0,0),(100,100)]

def threaded_client(conn,Player):
    conn.send(str.encode(make_pos(pos[Player])))
    reply=""
    while True:
        try:
            data=read_pos(conn.recv(2048).decode())
            pos[Player]=data
            if not data:
                print("Disconnected")
                break
            else:
                if Player==1:
                    reply=pos[0]
                else:
                    reply=pos[1]

                print("Recived:",data)
                print("Sending:",reply) 

            conn.sendall(str.encode(make_pos(reply)))
        except:
            break
    
    print("Lost connection")
    conn.close()

currestPlayer = 0
while True:
    conn,addr=s.accept()
    print("Connecting to:",addr)
    start_new_thread(threaded_client,(conn,currestPlayer))
    currestPlayer+=1