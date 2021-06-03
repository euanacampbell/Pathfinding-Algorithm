from __future__ import print_function
# Algorithm MapHandler
import time
from MapHandler.MapHandler import MapHandler
from Algorithms.newAlgorithmHandler import NBPAHandler
from Algorithms.dijkstra import dijkstra
from Algorithms.bfs import BFS
from Algorithms.dfs import DFS
from Algorithms.astar import *
from DataHandler.DataHandler import DataHandler

class IngestionEngine():

    #def __init__(self, noOfMaps, mapSize, iterations, algorithms):
    def __init__(self, mapRange, iterations, algorithmCode):
        print('')
        # Initiation
        self.sizeStart = mapRange[0]
        self.sizeFinish = mapRange[1]
        self.iterations = iterations
        # 0 = New, 1 = Dijkstra, 2 = BFS, 3 = DFS, 4 = A Star
        self.algorithms = algorithmCode   # [0,0,0,0,0] = nothing run, [1,1,1,1,1] = all run

        # Generate Maps
        self.mapsHandler = MapHandler()

        self.dataHandler = DataHandler()

        self.RunTests()


    def RunTests(self):

        no_of_tests = (self.sizeFinish - self.sizeStart + 1) * self.iterations

        currentMapSize = self.sizeStart
        testNumber = 0
        while currentMapSize != self.sizeFinish+1:
            iteration = 0
            for i in range( self.iterations ):
                iteration += 1
                testNumber += 1
                successfulTest = False
                while successfulTest == False:

                    message = '\rProgress (tests completed): {}/{} | Current map size: {}'.format(str(testNumber), str(no_of_tests), str(currentMapSize))
                    print(message, end="") 

                    # Place Holders
                    newTime = 0
                    newPath = 0
                    newPathLength = 0

                    dijkstraTime = 0
                    dijkstraPath = 0
                    dijkstraPathLength = 0

                    bfsTime = 0
                    bfsPath = 0
                    bfsPathLength = 0

                    dfsTime = 0
                    dfsPath = 0
                    dfsPathLength = 0

                    astarTime = 0
                    astarPath = 0
                    astarPathLength = 0

                    map = self.mapsHandler.CreateMap(currentMapSize)

		    testStartTime = time.time()

                    if self.algorithms[0] == "1":
                        """NEW ALGORITHM"""

                        handler = NBPAHandler( map['arrayMap'], [ map["startY"], map["startX"], map["finishY"], map["finishX"] ] )
                        start_time = time.time()   # Start timer
                        route = handler.Run()   # Run map on algorithm
                        finish_time = time.time()   # Finish timer
                        timeTaken = finish_time - start_time   # Calculate runtime

                        newTime = timeTaken
                        newPath = route
                        newPathLength = len( route )

                    if self.algorithms[1] == "1":
                        """DIJKSTRA"""

                        start_time = time.time()   # Start timer
                        route = dijkstra(map["startNumber"], map["finishNumber"], map["graphWeighted"])   # Run map on algorithm
                        finish_time = time.time()   # Finish timer

                        timeTaken = finish_time - start_time   # Calculate runtime

                        dijkstraTime = timeTaken
                        dijkstraPath = route
                        dijkstraPathLength = len( route )

                    if self.algorithms[2] == "1":
                        """BFS"""

                        start_time = time.time()   # Start timer
                        route = BFS(map["startNumber"], map["finishNumber"], map["graphUnweighted"])   # Run map on algorithm
                        finish_time = time.time()   # Finish timer

                        timeTaken = finish_time - start_time   # Calculate runtime

                        bfsTime = timeTaken
                        bfsPath = route
                        bfsPathLength = len( route )

                    if self.algorithms[3] == "1":
                        """DFS"""

                        start_time = time.time()   # Start timer
                        route = DFS(map["startNumber"], map["finishNumber"], map["graphUnweighted"])   # Run map on algorithm
                        finish_time = time.time()   # Finish timer

                        timeTaken = finish_time - start_time   # Calculate runtime

                        dfsTime = timeTaken
                        dfsPath = route
                        dfsPathLength = len( route )

                    if self.algorithms[4] == "1":
                        """A STAR"""

                        start_time = time.time()   # Start timer
                        route = AStarSetup(map["aStarMap"], [map["startY"],map["startX"],map["finishY"],map["finishX"]])
                        finish_time = time.time()   # Finish timer

                        timeTaken = finish_time - start_time   # Calculate runtime

                        astarTime = timeTaken
                        astarPath = route
                        astarPathLength = len( route )

		    testFinishTime = time.time()
	            testTime = testFinishTime - testStartTime

                    if astarPathLength != 0:
                        successfulTest = True

	            

                ideal = abs(map["startX"] - map["finishX"]) + abs(map["startY"] - map["finishY"])
                MapStorage = [testNumber, currentMapSize, iteration, ideal, testTime]

                ResultsStorage = [testNumber, newTime, newPathLength, dijkstraTime, dijkstraPathLength, bfsTime, bfsPathLength, dfsTime, dfsPathLength, astarTime, astarPathLength]

                self.dataHandler.AddData(MapStorage, ResultsStorage)

            currentMapSize += 1


start = time.time()
new = IngestionEngine([10,15], 500, ["1", "1", "0", "1", "1"])
finish = time.time()
time_taken = round(finish - start, 2)

print('\n\nTime taken: {} seconds'.format(time_taken))


"""
print("DFS")
for i in new.resultsDFS:
    print( i["NodesInFinalRoute"] )

print("BFS")
for i in new.resultsBFS:
    print( i["NodesInFinalRoute"] )

print("Dijkstra")
for i in new.resultsDijkstra:
    print( i["NodesInFinalRoute"] )

print("A Star")
for i in new.resultsAStar:
    print( i["NodesInFinalRoute"] )
"""

"""
print( "DIJKSTRA" )
for i in new.resultsDijkstra:
    print( i["NodesInFinalRoute"] )

print( "A STAR" )
for i in new.resultsAStar:
    print( i["NodesInFinalRoute"] )




print( "DIJKSTRA" )
otherList = []
for i in range( 10,31 ):
    newList = []
    for j in new.resultsDijkstra:
        if j["MapSize"] == i:
            newList.append(j["NodesInFinalRoute"])

    otherList.append( newList )

averages = []
for i in otherList:
    average = sum(i) / float(len(i))
    averages.append( average )

for i in averages:
    print( i )




print( "A STAR" )
otherList = []
for i in range( 10,31 ):
    newList = []
    for j in new.resultsAStar:
        if j["MapSize"] == i:
            newList.append(j["NodesInFinalRoute"])

    otherList.append( newList )

averages = []
for i in otherList:
    average = sum(i) / float(len(i))
    averages.append( average )

for i in averages:
    print( i )
"""
