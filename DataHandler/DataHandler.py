import csv

class DataHandler():

    def __init__(self):

        with open( 'maps.csv', 'w' ) as maps_file:
            fieldnames = [ "Test Number", "Map Size", "Iteration", "Ideal Path", "Completion Time"]
            csv_writer = csv.DictWriter(maps_file, fieldnames=fieldnames, delimiter=',')

            csv_writer.writeheader()


        with open( 'algorithm_results.csv', 'w' ) as algorithm_results_file:
            fieldnames = [ "Test Number", "newTime", "newPathLength", "dijkstraTime", "dijkstraPathLength", "bfsTime", "bfsPathLength", "dfsTime", "dfsPathLength", "astarTime", "astarPathLength"]
            csv_writer = csv.DictWriter(algorithm_results_file, fieldnames=fieldnames, delimiter=',')

            csv_writer.writeheader()


    def AddData(self, mapInfo, resultsInfo):

        with open( 'maps.csv', 'a' ) as maps_file:
            csv_writer = csv.writer(maps_file, delimiter=',')

            csv_writer.writerow( mapInfo )

        with open( 'algorithm_results.csv', 'a' ) as algorithm_results_file:
            csv_writer = csv.writer(algorithm_results_file, delimiter=',')

            csv_writer.writerow( resultsInfo )
