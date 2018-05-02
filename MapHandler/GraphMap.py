
class WeightedGraph():

    def __init__(self):
        """Initialisation of Graph instance"""

        self.noOfVertex = 0 # Holds the total number of nodes, not a necessity
        self.addList = {} # Holds all vertexes, edges and edge weights
        self.vertexValues = {}

    def addVertex(self, value): # vertex name
        """Takes name of vertex and creates a new item in the addList
        dictionary for storage"""

        # Checks to see if vertex already exists, vertex created if not
        if value not in self.addList:
            self.addList[value] = {}
            self.noOfVertex += 1
        else:
            print("Vertex already in graph")

    def addEdge(self, node1, node2, weight): # start node, end node, weight of edge
        """Using the existing nodes with the class, edges are added, with
        a weight added to the dictionary store"""

        # Checks to see if the edge already exists, edge created if not
        if node2 not in self.addList[node1]:
            self.addList[node1][node2] = weight
            self.addList[node2][node1] = weight

class UnweightedGraph():

    def __init__(self):
        self.noOfVertex = 0
        self.addList = {}
        self.vertexValues = {}

    def addVertex(self, value):
        """Adds a new vertex to the graph structure"""

        # If the vertex does not already exist in the adjacency list, create the vertex
        if value not in self.addList:
            self.addList[value] = [] # Stores new vertex as dictionary value
            self.noOfVertex += 1
        else:
            print("Vertex already in graph")

    def addEdge(self, node1, node2):
        """Creates an edge between two vertices, unweighted and undirectional"""

        # If the edge does not already exist in the adjacency list
        if node2 not in self.addList[node1]:
            # Applies edge to both vertices
            self.addList[node1].append(node2)
            self.addList[node2].append(node1)

        # Error returned if either vertex does not exist
