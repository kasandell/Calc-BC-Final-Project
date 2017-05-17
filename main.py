import os
import sys
import matplotlib.pyplot as plt
import numpy as np
from sources.dataHandler import dataHandler
from sources.integrator import integrator
from sources.serialReader import serialReader




if __name__ == '__main__':
    sr = serialReader('/dev/cu.usbmodem1421', 9600)
    dh = dataHandler()
    dh.addDataStream('acceleration')
    dh.addDataStream('velocity')
    dh.addDataStream('displacement')
    ig = integrator()
    try: 
        while True:
            val = sr.getline()
            ret = ig.integrate(val);
            dh.addToDataStream('acceleration', ret['acceleration'])
            dh.addToDataStream('velocity', ret['velocity'])
            dh.addToDataStream('displacement', ret['displacement'])

    except KeyboardInterrupt as k:
        xL, yL = dh.getPlottableVersion('acceleration')
        plt.plot(xL, yL, 'ro')
        print min(xL), max(xL), min(yL), max(yL)
        plt.axis(min(xL), max(xL), min(yL), max(yL))
        plt.show()
