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

#the server has stared 
s.listen(maxPlayerCount)
print("Wating for a connection,Server Started")


def threaded_client(conn):
    #first message showing the connection was succesful
    conn.send(str.encode("Connected"))
    reply=""
    while True:
        try:
            #meddage recived form the client
            data=conn.recv(2048)
            #the reply is the data that we recived 
            #we can use this reply to send more useful information in the future
            reply=data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Recived:",reply)
                print("Sending:",reply)
            #sending a reply back to the client according to the the meaadge that we recived 
            conn.sendall(str.encode(reply))
        except:
            break
    
    print("Lost connection")
    conn.close()

while True:
    conn,addr=s.accept()
    #prints the IP address of the client
    print("Connecting to:",addr)
    #creatring a threaded function so that the loop executin does not stop
    start_new_thread(threaded_client,(conn,))