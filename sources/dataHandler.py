

class dataHandler(object):
    def __init__(self):
        self.dataStreams = {}

    def addDataStream(self, dataStream):
        if dataStream not in self.dataStreams:
            self.dataStreams[dataStream] = []
   
    def addToDataStream(self, dataStream, dataObject):
        dataPair = (dataObject['time'], dataObject['value'])
        if dataStream in self.dataStreams:
            self.dataStreams[dataStream].append(dataPair)
        else:
            self.dataStreams[dataSteam] = [ dataPair ]

    def getPlottableVersion(self, dataStream):
        if dataStream in self.dataStreams:
            xList, yList = zip(*self.dataStreams[dataStream])
            #xList = [ x[0] for x in self.dataStreams[dataStream] ]
            #yList = [ y[1] for y in self.dataStreams[dataStream] ]
            return xList, yList


    def createPositionStream(self):
        pList = self.__dispToPos()
        return pList

                
    def __dispToPos(self):
        init = self.dataStreams['displacement'][0][1]
        fin = self.dataStreams['displacement'][-1][1]
        #TODO: check this math. it might be wrong to to absolute value
        delt = abs(fin-init)
        posList = [(x[0], x[1]+delt) for x in self.dataStreams['displacement']]
        self.dataStreams['position'] = posList
        return posList
