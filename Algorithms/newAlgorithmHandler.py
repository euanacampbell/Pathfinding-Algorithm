from Brain import Brain
import time

class NBPAHandler():

    def __init__(self, inputMap, startfinish):

        self.brain = Brain()
        self.map = inputMap

        self.currentH = startfinish[0]
        self.currentW = startfinish[1]

        self.relativeH = 1
        self.relativeW = 1

        self.finish = [ startfinish[2], startfinish[3] ]

        self.stuck = False

        self.found = False

        self.step = 0


    def Run(self):

        while True:
            self.step += 1

            self.brain.addNodeValues( self.AnalyseAround() )

            if self.stuck == True:
                return([])

            self.DetermineNextMove()

            if self.stuck == True:
                return([])

            if self.found == True:
                break

        return( self.brain.journey )

    def AnalyseAround(self):
        """Updates memory on locations surrounding current location """

        aroundMe = {"N":0, "E":0, "S":0, "W":0}

        try:
            if self.map[self.currentH+1][self.currentW] in [2,5,7]:
                aroundMe["S"] = self.WhatsAroundMe(self.currentH+1, self.currentW)
        except IndexError:
            pass
        try:
            if self.map[self.currentH-1][self.currentW] in [2,5,7]:
                aroundMe["N"] = self.WhatsAroundMe(self.currentH-1, self.currentW)
        except IndexError:
            pass
        try:
            if self.map[self.currentH][self.currentW+1] in [2,5,7]:
                aroundMe["E"] = self.WhatsAroundMe(self.currentH, self.currentW+1)
        except IndexError:
            pass
        try:
            if self.map[self.currentH][self.currentW-1] in [2,5,7]:
                aroundMe["W"] = self.WhatsAroundMe(self.currentH, self.currentW-1)
        except IndexError:
            pass

        analyser = 0
        for i in aroundMe:
            analyser += aroundMe[i]

        if analyser == 0:
            self.stuck = True

        return( aroundMe )



    def WhatsAroundMe(self, y, x):
        """Gets passed a node, feeds back the number of nodes that it can travel to. Used by AnalyseAround()"""

        value = 0
        try:
            if self.map[y+1][x] in [2,5,7]:
                value += 1
        except IndexError:
            pass

        try:
            if self.map[y-1][x] in [2,5,7]:
                value += 1
        except IndexError:
            pass

        try:
            if self.map[y][x+1] in [2,5,7]:
                value += 1
        except IndexError:
            pass

        try:
            if self.map[y][x-1] in [2,5,7]:
                value += 1
        except IndexError:
            pass

        return( value )

    def DetermineNextMove(self):
        """Using all information provided, determine in which location to travel next

        RULES:
        - Do not bother going to node with value of 1
        - Go to node if it reduces largest gap in X/Y differences and has a value of 4

        - Use backstack to keep track of previous nodes visited, can go back to those nodes if it gets stuck
            - Mark locations that have had to be backtracked from
        """

        difInY = abs( self.currentH - self.finish[0] )
        difInX = abs( self.currentW - self.finish[1] )
        if difInX == 0 and difInY == 0:
            self.found = True
            return( True )

        locations = ["N", "S", "E", "W"]
        opposites = {"N": "S","E": "W","S": "N","W": "E",}
        # Removes need to travel to nodes that will have a deadend
        try:
            if self.brain.memory[self.brain.currentLocationH+1][self.brain.currentLocationW] == 0 or self.brain.memory[self.brain.currentLocationH+1][self.brain.currentLocationW] == 1:
                locations.remove( "S" )
        except IndexError:
            pass
        try:
            if self.brain.memory[self.brain.currentLocationH-1][self.brain.currentLocationW] == 0 or self.brain.memory[self.brain.currentLocationH-1][self.brain.currentLocationW] == 1:
                locations.remove( "N" )
        except IndexError:
            pass
        try:
            if self.brain.memory[self.brain.currentLocationH][self.brain.currentLocationW+1] == 0 or self.brain.memory[self.brain.currentLocationH][self.brain.currentLocationW+1] == 1:
                locations.remove( "E" )
        except IndexError:
            pass
        try:
            if self.brain.memory[self.brain.currentLocationH][self.brain.currentLocationW-1] == 0 or self.brain.memory[self.brain.currentLocationH][self.brain.currentLocationW-1] == 1:
                locations.remove( "W" )
        except IndexError:
            pass

        aroundImportance = {}
        aroundImportance["S"] = difInY * self.brain.memory[self.brain.currentLocationH+1][self.brain.currentLocationW]
        aroundImportance["N"] = difInY * self.brain.memory[self.brain.currentLocationH-1][self.brain.currentLocationW]
        aroundImportance["E"] = difInX * self.brain.memory[self.brain.currentLocationH][self.brain.currentLocationW+1]
        aroundImportance["W"] = difInX * self.brain.memory[self.brain.currentLocationH][self.brain.currentLocationW-1]

        alternatives = []

        if self.currentH > self.finish[0] and "S" in locations:
            locations.remove( "S" )
            alternatives.append("S")
        if self.currentH < self.finish[0] and "N" in locations:
            locations.remove( "N" )
            alternatives.append("N")
        if self.currentW > self.finish[1] and "E" in locations:
            locations.remove( "E" )
            alternatives.append("E")
        if self.currentW < self.finish[1] and "W" in locations:
            locations.remove( "W" )
            alternatives.append("W")

        best = 0
        move = "B"
        for i in locations:
            if aroundImportance[i] > best:
                move = i
                best = aroundImportance[i]

        if move != "B":
            self.Move(move)
            return()

        if move == "B":
            pathToTake = self.FindWhenStuck()
            if self.stuck == True:
                return()
            for i in pathToTake:
                self.Move( i )
            return()

        if self.currentH == self.finish[0] and self.currentW == self.finish[1]:
            self.found = True
            return()



    def FindWhenStuck(self):
        """Will return the path to a location where the current location can be closer
        to the finish location

        Right will work anti-clockwise around a wall
        Left will work clockwise around a wall

        2 = good
        1 = bad"""



        directions = ["N", "E", "S", "W"]
        isolated = True
        for i in directions:
            if self.CanMove( i, self.currentH, self.currentW ) == True:
                isolated = False
        if isolated == True:
            return()


        difInY = abs( self.currentH - self.finish[0] )
        difInX = abs( self.currentW - self.finish[1] )

        rightDif = [ difInY, difInX ]
        leftDif = [ difInY, difInX ]

        rightDifInY = difInY
        rightDifInX = difInX
        leftDifInY = difInY
        leftDifInX = difInX

        rightHistory = []
        leftHistory = []

        rightPointer = ""
        leftPointer = ""

        rightLocations = [self.currentH, self.currentW]
        leftLocations = [self.currentH, self.currentW]

        tryRight = {"N":"W", "W":"S", "S":"E", "E":"N"}
        otherwiseRight = {"N":"E", "E":"S", "S":"W", "W":"N"}

        tryLeft = {"N":"E", "E":"S", "S":"W", "W":"N"}
        otherwiseLeft = {"N":"W", "W":"S", "S":"E", "E":"N"}

        if difInX > difInY:
            if self.currentW > self.finish[1]:
                rightPointer = "N"
                leftPointer = "S"
            else:
                rightPointer = "S"
                leftPointer = "N"
        else:
            if self.currentH > self.finish[0]:
                rightPointer = "E"
                leftPointer = "W"
            else:
                rightPointer = "W"
                leftPointer = "E"
        counter = 0
        while True:
            counter += 1
            if self.CanMove( rightPointer, rightLocations[0], rightLocations[1] ) == True:
                break
            else:
                rightPointer = otherwiseRight[rightPointer]

            if counter == 4:
                self.stuck = True
                return()
        counter = 0
        while True:
            counter += 1
            if self.CanMove( leftPointer, leftLocations[0], leftLocations[1] ) == True:
                break
            else:
                leftPointer = otherwiseLeft[leftPointer]

            if counter == 4:
                self.stuck = True
                return()

        counter = 10
        for i in range(counter):
            if abs( rightLocations[0] - self.finish[0] ) < difInY and abs( rightLocations[1] - self.finish[1] ):
                return( rightHistory )
            elif abs( leftLocations[0] - self.finish[0] ) < difInY and abs( leftLocations[1] - self.finish[1] ):
                return( leftHistory )
            else:
                counter += 1

            rMoveMade = False

        foundCloser = False

        while foundCloser == False:
            rightMove = { "N":[ rightLocations[0]-1 , rightLocations[1] ], "E":[ rightLocations[0] , rightLocations[1]+1 ], "S":[ rightLocations[0]+1 , rightLocations[1] ], "W":[ rightLocations[0] , rightLocations[1]-1 ] }
            leftMove = { "N":[ leftLocations[0]-1 , leftLocations[1] ], "E":[ leftLocations[0] , leftLocations[1]+1 ], "S":[ leftLocations[0]+1 , leftLocations[1] ], "W":[ leftLocations[0] , leftLocations[1]-1 ] }

            rightDifMove = { "N":[ rightDif[0]-1 , rightDif[1] ], "E":[ rightDif[0] , rightDif[1]+1 ], "S":[ rightDif[0]+1 , rightDif[1] ], "W":[ rightDif[0] , rightDif[1]-1 ] }
            leftDifMove = { "N":[ leftDif[0]-1 , leftDif[1] ], "E":[ leftDif[0] , leftDif[1]+1 ], "S":[ leftDif[0]+1 , leftDif[1] ], "W":[ leftDif[0] , leftDif[1]-1 ] }

            rMoveMade = False
            lMoveMade = False

            # RIGHT ARM DECISION
            while rMoveMade == False:
                if self.CanMove( tryRight[rightPointer], rightLocations[0], rightLocations[1] ):
                    rightHistory.append( tryRight[rightPointer] )
                    rightLocations = rightMove[tryRight[rightPointer]]
                    rightPointer = tryRight[rightPointer]

                    rMoveMade = True

                elif self.CanMove( rightPointer, rightLocations[0], rightLocations[1] ):
                    rightHistory.append( rightPointer )
                    rightLocations = rightMove[rightPointer]
                    rightPointer = rightPointer

                    rMoveMade = True

                else:
                    rightPointer = otherwiseRight[rightPointer]

            # LEFT ARM DECISION
            while lMoveMade == False:
                if self.CanMove( tryLeft[leftPointer], leftLocations[0], leftLocations[1] ):
                    leftHistory.append( tryLeft[leftPointer] )
                    leftLocations = leftMove[tryLeft[leftPointer]]
                    leftPointer = tryLeft[leftPointer]

                    lMoveMade = True

                elif self.CanMove( leftPointer, leftLocations[0], leftLocations[1] ):
                    leftHistory.append( leftPointer )
                    leftLocations = leftMove[leftPointer]
                    leftPointer = leftPointer

                    lMoveMade = True

                else:
                    leftPointer = otherwiseLeft[leftPointer]

                # Catch if impossible to find

                #if current right location in left location history:
                    #return( False )
            rightDif[0] = abs( rightLocations[0] - self.finish[0] )
            rightDif[1] = abs( rightLocations[1] - self.finish[1] )

            leftDif[0] = abs( leftLocations[0] - self.finish[0] )
            leftDif[1] = abs( leftLocations[1] - self.finish[1] )

            if rightDif[0] + rightDif[1] < difInY + difInX:
                foundCloser = True
                return( rightHistory )

            if leftDif[0] + leftDif[1] < difInY + difInX:
                foundCloser = True
                return( leftHistory )

            if (rightLocations[0] == self.currentH and rightLocations[1] == self.currentW) or (leftLocations[0] == self.currentH and leftLocations[1] == self.currentW):
                self.stuck = True
                return()

    def CanMove(self, direction, locationH, locationW):
        if direction == "N":
            if self.map[locationH-1][locationW] == 2:
                return( True )
            else:
                return( False )
        if direction == "S":
            if self.map[locationH+1][locationW] == 2:
                return( True )
            else:
                return( False )
        if direction == "E":
            if self.map[locationH][locationW+1] == 2:
                return( True )
            else:
                return( False )
        if direction == "W":
            if self.map[locationH][locationW-1] == 2:
                return( True )
            else:
                return( False )

    def Move(self, move):

        if move == "S":
            self.currentH += 1
            self.relativeH += 1
        if move == "N":
            self.currentH -= 1
        if move == "E":
            self.currentW += 1
            self.relativeW += 1
        if move == "W":
            self.currentW -= 1
        if move == "B":
            pass

        self.brain.backstack.append(move)
        self.brain.makingAMove(move)


def GraphicalPrint(inputmap):
    for j in inputmap:
        print( "" )
        for k in j:
            if k == 0 or k == 1:
                print "#",
            elif k == 5:
                print ">",
            elif k == 7:
                print "@",
            else:
                print ".",
