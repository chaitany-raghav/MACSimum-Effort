import socket
from _thread import *
import sys

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


def threaded_client(conn):
    reply=""
    while True:
        try:
            data=conn.recv(2048)
            reply=data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Recived:",reply)
                print("Sending",reply)
        
            conn.sendall(str.encode(reply))
        except:
            break
        

while True:
    conn=addr=s.accept()
    print("Connecting to:",addr)

    start_new_thread(threaded_client(conn))