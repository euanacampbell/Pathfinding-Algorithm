

class Brain():

    def __init__(self):

        self.currentLocationH = 1
        self.currentLocationW = 1
        self.backstack = []

        self.journey = []

        self.memory = [[0,0,0],
                       [0,0,0],
                       [0,0,0]]

    def makingAMove(self, direction):
        """Changes the current location reference marker"""

        self.journey.append(direction)
        if direction == "N":
            if self.currentLocationH == 1:
                self.increaseTop()
                self.currentLocationH = 1
            else:
                self.currentLocationH -= 1

        if direction == "E":
            if self.currentLocationW + 2 == len(self.memory[0]):
                self.increaseRight()

            self.currentLocationW += 1

        if direction == "S":
            if self.currentLocationH + 2 == len(self.memory):
                self.increaseBottom()

            self.currentLocationH += 1

        if direction == "W":
            if self.currentLocationW == 1:
                self.increaseLeft()
                self.currentLocationW = 1
            else:
                self.currentLocationW -= 1


    def addNodeValues(self, travels):
        """Adds values to nodes around current location"""

        self.memory[self.currentLocationH - 1][self.currentLocationW] = travels["N"]
        self.memory[self.currentLocationH + 1][self.currentLocationW] = travels["S"]
        self.memory[self.currentLocationH][self.currentLocationW + 1] = travels["E"]
        self.memory[self.currentLocationH][self.currentLocationW - 1] = travels["W"]

        #self.memory[self.currentLocationH][self.currentLocationW] = 9

    def increaseTop(self):
        toAdd = []
        for i in range(len(self.memory[0])):
            toAdd.append(0)
        self.memory.insert(0, toAdd)

    def increaseRight(self):
        for i in self.memory:
            i.append(0)

    def increaseBottom(self):
        newRow = []
        for i in range(len(self.memory[0])):
            newRow.append(0)

        self.memory.append(newRow)

    def increaseLeft(self):
        for i in self.memory:
            i.insert(0,0)
