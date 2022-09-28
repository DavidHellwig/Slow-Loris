import socket

class Attacker:
    def __init__(self,target):
        self.target = target
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

    def attackTarget(self):
        pass

    def stayAlive(self):
        pass

    def printStatus(self):
        pass


