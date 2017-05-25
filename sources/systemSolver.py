import dataHandler
import numpy as np
import random




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
        print 'idx range: ', indexRange
        lst = []
        equals = []
        for x in indexRange:
            eq = [self.accList[x], self.velList[x], self.posList[x]]
            lst.append(eq)
            equals.append(0)
        print 'lst: ', lst
        print 'equals: ', equals
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
        _, pos = self.dh.getPlottableVersion('position')
        return acc, vel, pos
        
    #whole time program is running, we calculate the displacement, but we really want to have this in terms of position relative to the zero position of the spring, so use first and last values as approximation of spring stretched
    #TODO: edit to solve random selection of three, so that they are far enough apart to give real coefficients`
    def solveSystem(self):
        self.accList, self.velList, self.posList = self.__getData()
        '''
        data = np.concatenate( (self.accList[:, np.newaxis], self.velList[:, np.newaxis], self.posList[:, np.newaxis]) , axis=1)
        print 'data: ', data
        datamean = data.mean(axis=0)
        uu, dd, vv = np.linalg.svd(data - datamean)
        print vv[0]
        '''
        mx = max(self.accList)
        mn = min(self.accList)
        deltIdx = abs( self.accList.index(mn)  - self.accList.index(mx) )
        for x in range(0, len(self.accList) - deltIdx): 
            vals = (x, x + (deltIdx/2), x + deltIdx)
            m, c, k = self.__solveOne(vals)
            self.massList.append(m)
            self.springList.append(k)
            self.dampList.append(c)
        avgMass = sum(self.massList)/len(self.massList)
        avgSpring = sum(self.springList)/len(self.springList)
        avgDamp = sum(self.dampList)/len(self.dampList)
        return avgMass, avgDamp, avgSpring
        
        


