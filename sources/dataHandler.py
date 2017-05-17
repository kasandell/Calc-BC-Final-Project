

class dataHandler(object):
    def __init__(self):
        self.dataStreams = {}

    def addDatastream(self, dataStream):
        if dataStream not in self.dataStreams:
            self.dataStreams[dataStream] = []
   
    def adToDataStream(self, dataStream, dataPair):
        if dataStream in self.dataStreams:
            self.dataStreams[dataStream].append(dataPair)
        else:
            self.dataStreams[dataSteam] = [ dataPair ]

    def getPlottableVersion(self, dataStream):
        if dataStream in self.dataStreams:
            xList, yList = [x[0], x[1] for x in self.dataStreams[dataStream] ]
            return xList, yList

            
