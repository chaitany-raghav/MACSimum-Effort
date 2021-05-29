import socket


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server = "10.0.0.2"
        self.port = 5555
        self.addr = (self.server,self.port)
        #id will contain the information sent the the server
        #It acts as a basic Acknoledgemnt that the connecton was succesful
        self.id = self.connect()
        print(self.id)

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self,data):
        try:
            #sending the data to the server
            self.client.send(str.encode(data))
            #returning the meaasge recived bt the server
            return self.client.recv(2048).decode()

        except socket.error as e:
            print(e)



n=Network()
print(n.send("Hello"))
print(n.send("Working"))