

'''assumptions made:
    we are integrating over such miniscule time periods every time (like one millisecond), that it does not matter if we do a left, right, or midpoint reimann sum
    We are already so close to being basically the actual integral that the error won't be of any issue
    when integrating from velocity to displacement, even though we use the newly calculated velocity, it should, in theory, be not that much different from the last one, so it won't makde
    any noticable error. If it does, we can always average to make it better
    '''

class integrator(object):
    def __init__(self):
        self.lastTime = 0.0
        self.initTime = 0.0
        self.totalVelocity = 0.0
        self.totalDisplacement = 0.0
        self.millisToSec = float(1.0/1000.0)
        self.lastAccel = 0.0
        self.lastVel = 0.0
        self.lastDisp = 0.0


    def setInitTime(self, initTime):
        self.initTime = initTime

    def __getElapsedTime(self, newTime):
        return (newTime - self.initTime)

    def integrate(self, accelData):
        if self.initTime is 0:
            #set the initial time this program starts integrating from
            self.initTime = accelData['time'] * self.millisToSec
            self.lastTime = accelData['time'] * self.millisToSec
            #return 0 displacement, velocity, and acceleration
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
            newTime = float(accelData['time'] * self.millisToSec)
            accelVal = accelData['acceleration']

            rDict = {}
            #calculate the total elapsed time since we started running
            totalElapsedTime = self.__getElapsedTime(newTime)
            #save the acceleration value at elapsed time
            rDict['acceleration'] = {'value':accelVal, 'time': totalElapsedTime}
            #calucluate the small dt to integrate the acceleration into velocity, and the velocity into displacement
            deltaTime = newTime - self.lastTime

            #calculate fnInt(a)dt to get change in velocity 
            dVelocity = (accelVal + self.lastAccel)/2.0 * deltaTime
            print 'change in velocity: ', dVelocity
            #update the total velocity of the object
            preTotalVel =  self.totalVelocity
            self.totalVelocity = self.totalVelocity + dVelocity 
            #save the total velocity at this time
            rDict['velocity'] = {'value': self.totalVelocity, 'time': totalElapsedTime}

            #calculuate fnInt(v)dt to get change in displacement
            #TODO: if program is erroneous in calculations, it's probably this line. replace total velocity with an average of last velocity and new velocity for better estimate
            dDisplacement = (self.lastAccel + accelVal) / 2.0 * deltaTime * deltaTime#(self.totalVelocity + preTotalVel) / 2.0 * deltaTime
            #update total displacement
            self.totalDisplacement = self.totalDisplacement + dDisplacement
            #save total displacement
            rDict['displacement'] = {'value': self.totalDisplacement, 'time': totalElapsedTime}
            #this is the last time we were at, so integrate from this point next iteration
            self.lastTime = newTime
            #return data 
            self.lastAccel = accelVal
            return rDict
