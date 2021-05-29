import socket


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #The ip of the server
        self.server = "10.0.0.2"
        self.port = 5555
        self.addr = (self.server,self.port)
        #get the initial position of the object
        self.pos = self.connect()
    
    def getPos(self):
        return self.pos

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self,data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()

        except socket.error as e:
            print(e)

