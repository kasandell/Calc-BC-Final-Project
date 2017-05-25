import serial



#read data over the serial port
#getline returns a map of data, and expects the line to be in the format of timestamp,acceleration

class serialReader(object):
    def __init__(self, com, baudrate):
        self.serial = serial.Serial()
        self.serial.baudrate = baudrate
        self.serial.port = com
        self.open()
        self.serial.flush()
        self.isOpen = self.serial.is_open
        self.accelAdjustment = -9.81

    def isOpen(self):
        return self.isOpen

    def open(self):
        self.serial.open()

    def close(self):
        self.serial.close()

    def getline(self):
        #read two ints from the com port: accelerometer value, and time
        line = self.serial.readline()
        parts = [float(x) for x in line.strip().split(',')]
        dct = {'time': parts[0], 'acceleration':float( format( (1000 * (parts[1] - self.accelAdjustment) - -730.0 -10.0), '.4f')) }
        print 'read: ', dct
        return dct
