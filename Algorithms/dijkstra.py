def dijkstra(start, finish, addList):
    """Generates the tentative weights for all values on the graph
    Then uses the genPath function to produce the path from the start
    node to the finish"""

    current = start
    tenWeight = {}
    pre = {}
    visited = []

    for i in addList:
        tenWeight[i] = float("inf")
        pre[i] = None

    tenWeight[start] = 0

    while current != finish:
        tmp = addList[current]

        for i in tmp:
            if tenWeight[current] + tmp[i] < tenWeight[i]:
                tenWeight[i] = tenWeight[current] + tmp[i]
                pre[i] = current

        if current not in visited:
            visited.append(current)
        else:
            return([])
        mini = float("inf")

        for i in addList:
            if (i not in visited) and (tenWeight[i] < mini):
                current = i
                min
                i = tenWeight[i]


    visited.append(finish)
    path = genPath(pre, finish)
    return( path[::-1] )

def genPath(pre, finish):
    """Used by the 'dijkstra' algorithm to produce a list containing the best
    path from the start location to the finish"""

    result = []

    while pre[finish] != None:
        result.append(finish)
        finish = pre[finish]

    result.append(finish)
    return result

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
