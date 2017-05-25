import os
import sys
import matplotlib.pyplot as plt
import numpy as np
import random
from sources.dataHandler import dataHandler 
from sources.integrator import integrator
from sources.serialReader import serialReader
from sources.systemSolver import systemSolver
from sources.recorder import recorder




if __name__ == '__main__':
    sr = serialReader('/dev/cu.usbmodem1421', 9600)
    dh = dataHandler()
    dh.addDataStream('acceleration')
    rc = recorder()
    try: 
        while True:
            val = sr.getline()
            adjust = rc.record(val) #adjust accelerationData 
            dh.addToDataStream('acceleration', adjust)

    except KeyboardInterrupt as k:
        sr.close()
        ig = integrator(dh)
        dh = ig.integrate()
        '''
        sysSolver = systemSolver(dh)
        mass, dampConst, springConst = sysSolver.solveSystem()
        print 'Mass: ', mass
        print 'Damping Constant: ', dampConst
        print 'Spring Constant: ', springConst
        '''
        

        time, acc = dh.getPlottableVersion('acceleration')
        _, vel = dh.getPlottableVersion('velocity')
        _, disp = dh.getPlottableVersion('displacement')
        _, pos = dh.getPlottableVersion('position')
        

        begin, end = int(len(acc) * .125), int(len(acc) *.3)
        rand1 = random.randint(begin, end)
        rand2 = random.randint(begin, end)
        rand3 = random.randint(begin, end)


        print 'Acceleration: ', acc[rand1], acc[rand2], acc[rand3]
        print 'Velocity: ',  vel[rand1], vel[rand2], vel[rand3]
        print 'Position: ', pos[rand1], pos[rand2], pos[rand3]
        maxFirst = max(acc)
        maxIdx1 = acc.index(maxFirst)
        maxSecond = max(acc[maxIdx1+1:])
        maxIdx2 = acc.index(maxSecond)
        pd = time[maxIdx2] - time[maxIdx1]
        print 'Period: ', pd

        minXAxis, maxXAxis = min(time), max(time)
        minAcc, maxAcc = min ( acc ) - 1000, max(acc) + 1000
        minVel, maxVel = min(vel) - 1000, max(vel) + 1000
        minDisp, maxDisp = min(disp) - 1000, max(disp) + 1000
        minPos, maxPos = min(pos) -1000, max(pos) + 1000

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
