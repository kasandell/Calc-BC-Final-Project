

class integrator(object):
    def __init__(self):
        self.initAccelTime = 0
        self.lastAccelTime = 0

        self.totalVeloc = 0
        self.lastVelocTime = 0

         
        self.totalDisp = 0

    def setInitTime(self, initTime):
        self.initAccelTime = initTime

    def integrate(self, data, type="a"):
        if type is 'a':
            #do shit
        elif type is 'v':
            #do velocity shit
        elif type is 'd':
            #do displacement shit

