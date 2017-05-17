

class integrator(object):
    def __init__(self):
        self.lastAccel = 0
        self.lastVeloc = 0
        self.lastDisp = 0
        self.lastAccelTime = 0
        self.lastVelocTime = 0
        self.lastDispTime = 0
        self.initTimeRun = 0
        self.totalVeloc = 0
        self.totalDisp = 0


    def setInitTime(self, initTime):
        self.initTimeRun = initTime

    def integrate(self, accelData):
        if self.initTimeRun is 0:
            self.initTimeRun = accelData['time']
            self.lastAccelTime = accelData['time']
            return {    
                    'acceleration': {
                        'value': 0,
                        'time': 0
                    },
                    'velocity': {
                        'value': 0,
                        'time': 0
                    },
                    'displacement': {
                        'value': 0,
                        'time': 0
                    }
                }
        else:
            newAccelTime = accelData['time']
            newAccelVal = accelData['acceleration']
            rDict = {}
            totalDeltAccelTime = newAccelTime - self.initTimeRun
            rDict['acceleration'] = { 'value': newAccelVal, 'time': newAccelTime }
            #integrate acceleration to get velocity
            deltAccelTime = newAccelTime - self.lastAccelTime

            deltVelocity  = deltAccelTime * newAccelVal

            self.totalVeloc = self.totalVeloc + deltVelocity
            totalDeltVelocTime = self.lastAccelTime + (deltAccelTime/2)
            #save to dict
            rDict['velocity'] = {'value': self.totalVeloc, 'time': totalDeltVelocTime}

            #integrate veloc for disp
            deltVelocTime = totalDeltVelocTime - self.lastVelocTime

            deltDisp = self.totalVeloc * deltVelocTime
            self.totalDisp = self.totalDisp + deltDisp
            totalDeltDispTime = self.lastVelocTime + (deltVelocTime/2)
            rDict['displacement'] = {'value': self.totalDisp, 'time': totalDeltDispTime}
            self.lastVelocTime = totalDeltVelocTime
            self.lastDispTime = totalDeltDispTime
            self.lastAccelTime = totalDeltAccelTime
            return rDict



            

