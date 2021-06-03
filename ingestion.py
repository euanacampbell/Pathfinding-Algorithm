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
    def __init__(self, mapRange, iterations, algorithmCode, results_print=False):
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

        # Run everything
        start = time.time()
        self.run()
        finish = time.time()
        time_taken = round(finish - start, 2)
        if results_print:

            algorithm_lookup = {
                0: 'New',
                1: 'Dijkstra',
                2: 'BFS',
                3: 'DFS',
                4: 'A*'
            }
            algorithms=[]
            for i in range(0, len(algorithmCode)):
                if int(algorithmCode[i])==1:
                    algorithms.append(algorithm_lookup[i])

            print('\n\n')
            print('Algorithms: {}'.format(', '.join(algorithms)))
            print('Maps sizes: {} -> {}'.format(self.sizeStart, self.sizeFinish))
            print('Iterations: {}'.format(self.iterations))
            print('Time taken: {} seconds'.format(time_taken))
    
    def run(self):

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

                    message = '\rTests completed: {}/{} | Current map size: {}/{}'.format(str(testNumber), str(no_of_tests), str(currentMapSize), str(self.sizeFinish))
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



if __name__=="__main__":

    new = IngestionEngine([10,12], 500, ["1", "1", "0", "1", "1"], results_print=True)
