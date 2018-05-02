#import profile
from CaveGeneration import CA_CaveFactory
from random import randint
from GraphMap import WeightedGraph,UnweightedGraph

class MapHandler():

    def __init__(self):
        self.arrayMap = []
        self.graphmapWeighted = []
        self.graphmapUnweighted = []
        self.astarmap = []

        self.startfinish = []
        self.startNumber = 0
        self.finishNumber = 0



    def CreateMap(self, mapSize):
        self.mapSize = mapSize
        self.GenerateCaveMaps(mapSize)
        self.ConvertToGraphMap( self.arrayMap )
        self.ConvertToAStarMap( self.arrayMap )

        self.mapDetails = {}

        self.mapDetails["mapSize"] = mapSize
        self.mapDetails["arrayMap"] = self.arrayMap
        self.mapDetails["graphWeighted"] = self.graphmapWeighted.addList
        self.mapDetails["graphUnweighted"] = self.graphmapUnweighted.addList
        self.mapDetails["aStarMap"] = self.astarmap
        self.mapDetails["startX"] = self.startfinish[1]
        self.mapDetails["startY"] = self.startfinish[0]
        self.mapDetails["finishX"] = self.startfinish[3]
        self.mapDetails["finishY"] = self.startfinish[2]
        self.mapDetails["startNumber"] = self.startNumber
        self.mapDetails["finishNumber"] = self.finishNumber

        #self.GraphicalPrint( self.arrayMap )
        #print("")
        return( self.mapDetails )



    def GenerateCaveMaps(self, size):

        newMap = CA_CaveFactory(size,size,0.41)
        newMap.gen_map()
        newMap = newMap.map
        finishedMap = self.AssignStartandFinish( newMap )

        self.arrayMap = finishedMap

    def GraphicalPrint(self, arrayMap):
        for i in arrayMap:
            for j in i:
                if j == 0 or j == 1:
                    print "#",
                elif j == 5:
                    print ">",
                elif j == 7:
                    print "@",
                else:
                    print ".",
            print( "" )


    def AssignStartandFinish(self, newMap):
        """5 = start, 7 = finish"""

        falseLocation = True
        while falseLocation:
            startX = randint(2, self.mapSize-3)
            startY = randint(2, self.mapSize-3)

            if newMap[startY][startX] == 2:
                falseLocation = False

        falseLocation = True
        while falseLocation:
            finishX = randint(0, self.mapSize-1)
            finishY = randint(0, self.mapSize-1)

            if newMap[finishY][finishX] == 2 and (finishX != startX and finishY != startY):
                falseLocation = False


        self.startfinish = [startY, startX, finishY, finishX]

        self.startNumber = (startX + 1) + (len(newMap) * startY)
        self.finishNumber = (finishX + 1) + (len(newMap) * finishY)



        return( newMap )
    def ConvertToAStarMap(self, arraymap):
        newMap = []
        for i in arraymap:
            newRow = []
            for j in i:
                if j == 0:
                    newRow.append(1)
                elif j == 2:
                    newRow.append(0)
                elif j == 5:
                    newRow.append(0)
                elif j == 7:
                    newRow.append(0)
                else:
                    newRow.append(1)
            newMap.append( newRow )

        self.astarmap = newMap




    def ConvertToGraphMap(self, arraymap):
        newWeightedGraph = WeightedGraph()
        newUnweightedGraph = UnweightedGraph()
        counter = 0

        for i in arraymap:
            for j in i:
                counter += 1
                if j in [2,5,7]:
                    newWeightedGraph.addVertex(counter)
                    newWeightedGraph.vertexValues[counter] = j

                    newUnweightedGraph.addVertex(counter)
                    newWeightedGraph.vertexValues[counter] = j

        for i in newWeightedGraph.vertexValues:
            try:
                if newWeightedGraph.vertexValues[i+self.mapSize] in [2,5,7]:
                    newWeightedGraph.addEdge(i, i+self.mapSize, 0)
                    newUnweightedGraph.addEdge(i, i+self.mapSize)
            except IndexError:
                pass
            except KeyError:
                pass

            try:
                if newWeightedGraph.vertexValues[i-self.mapSize] in [2,5,7]:
                    newWeightedGraph.addEdge(i, i-self.mapSize, 0)
                    newUnweightedGraph.addEdge(i, i-self.mapSize)
            except IndexError:
                pass
            except KeyError:
                pass

            try:
                if newWeightedGraph.vertexValues[i+1] in [2,5,7]:
                    newWeightedGraph.addEdge(i, i+1, 0)
                    newUnweightedGraph.addEdge(i, i+1)
            except IndexError:
                pass
            except KeyError:
                pass

            try:
                if newWeightedGraph.vertexValues[i-1] in [2,5,7]:
                    newWeightedGraph.addEdge(i, i-1, 0)
                    newUnweightedGraph.addEdge(i, i-1)
            except IndexError:
                pass
            except KeyError:
                pass

        self.graphmapWeighted = newWeightedGraph
        self.graphmapUnweighted = newUnweightedGraph
