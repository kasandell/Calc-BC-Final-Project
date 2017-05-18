import dataHandler
import numpy as np



class systemSolver(object):
    def __init__(self, dh):
        self.dh = dh
        self.accList = None
        self.velList = None
        self.posList = None
        self.massList = []
        self.dampList = []
        self.springList = []

    def __solveOne(self, indexRange):
        lst = []
        equals = []
        for x in indexRange:
            eq = [self.accList[x], self.velList[x], self.posList[x]]
            lst.append(eq)
            equals.append(0)

        npList = np.array(lst)
        npEquals = np.array(equals)
        solved = np.linalg.solve(npList, npEquals)
        #solved is in the form of mass, damping constant, spring constant 
        return solved[0], solved[1], solved[2]


        #get three values from each list, according to the index range
        #format them into matrices to fit np.linalg.solve ( 'https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.solve.html')
        #solve
        #return m(mass), c(damping coefficient, k(spring constant)



    def __getData(self):
        _, acc = self.dh.getPlottableVersion('acceleration')
        _, vel = self.dh.getPlottableVersion('velocity')
        _, disp = self.dh.getPlottableVersion('displacement')
        pos = self.__dispToPos(disp)
        return acc, vel, pos
        
    #whole time program is running, we calculate the displacement, but we really want to have this in terms of position relative to the zero position of the spring, so use first and last values as approximation of spring stretched
    def __dispToPos(self, dispList):
        init = dispList[0]
        fin = dispList[-1]
        #TODO: check this math. it might be wrong to to absolute value
        delt = abs(fin-init)
        dispList = [x+delt for x in dispList]
        return dispList

    def solveSystem(self):
        self.accList, self.velList, self.posList = self.__getData()

        #zip to prevent going to values that don't exist
        zipList = zip(self.accList, self.velList, self.dispList)

        for x in xrange(2, len(zipList)):
            indexRange = range( (x-2), x)
            m, c, k = self.__solveOne(indexRange)
            self.massList.append(m)
            self.dampList.append(c)
            self.sprintList.append(k)
        #average m, c, and k and return values
        avgMass = sum(self.massList)/len(self.massList)
        avgDamp = sum(self.dampList)/len(self.dampList)
        avgSpring = sum(self.springList)/len(self.springList)
        return avgMass, avgDamp, avgSpring

