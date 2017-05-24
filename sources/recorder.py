



class recorder(object):
    def __init__(self):
        self.initTime = None
        self.millisToSec = float(1.0/1000.0)


    def record(self, accelData):
        if not self.initTime:
            self.initTime = float(accelData['time'])
            return {'time': 0.0, 'value': accelData['acceleration'] } #0.0
        else:
            elapsedTime = float(accelData['time'] - self.initTime) * self.millisToSec * 1.0
            return {'time': elapsedTime, 'value': accelData['acceleration'] }

