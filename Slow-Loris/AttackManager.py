from Attacker import Attacker
class AttackManager:
    def __init__(self,target,numSockets):
        self.target = target
        self.socketCount = numSockets
        self.slowLoris = Attacker(self.target,self.socketCount)

        self.attackIsActive = False

    #Show the current status of the attack
    def checkAttackStatus(self):
        if(self.attackIsActive == True):
            statuses = []

            for loris in self.slowLoris.sockets:
                statuses.append(loris.returnStatus())

        elif(self.attackIsActive == False):
            return "Current Status: There is no attack occuring"
        else:
            return "Error: Something is broken"
