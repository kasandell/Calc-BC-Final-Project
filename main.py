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
        dh.createPositionStream()
        sr.close()
        time, acc = dh.getPlottableVersion('acceleration')
        print 'accel: ', acc
        _, vel = dh.getPlottableVersion('velocity')
        print 'veloc: ', vel
        _, disp = dh.getPlottableVersion('displacement')
        print 'disp: ', disp
        _, pos = dh.getPlottableVersion('position')
        print 'pos: ', pos
        minXAxis, maxXAxis = min(time), max(time)
        minAcc, maxAcc = min ( acc ), max(acc)
        minVel, maxVel = min(vel), max(vel)
        minDisp, maxDisp = min(disp), max(disp)
        minPos, maxPos = min(pos), max(pos)

        plt.figure(1)
        plt.title('Acceleration')
        plt.ylabel('acceleration')
        plt.xlabel('time')
        plt.axis([minXAxis, maxXAxis, minAcc, maxAcc])
        plt.plot(time, acc, 'b--')

        plt.figure(2)
        plt.title('Velocity')
        plt.ylabel('velocity')
        plt.xlabel('time')
        plt.axis([minXAxis, maxXAxis, minVel, maxVel])
        plt.plot(time, vel, 'r--')

        plt.figure(3)
        plt.title('Displacement')
        plt.ylabel('displacement')
        plt.xlabel('time')
        plt.axis([minXAxis, maxXAxis, minDisp, maxDisp])
        plt.plot(time, disp, 'g--')

        plt.figure(4)
        plt.title('Position')
        plt.ylabel('position')
        plt.xlabel('time')
        plt.axis([minXAxis, maxXAxis, minPos, maxPos])
        plt.plot(time, pos, 'y--')

        plt.show()
