def BFS(first, finish, addList):
    """Performs a Breadth-First-Search on the graph structure, outputs
    list of vertices"""

    Q = [first]
    visited = []

    while len(Q) > 0 and len(visited) != len( addList ):
        vertex = Q.pop()

        if vertex not in visited:
            visited.append(vertex)

            if finish in visited:
                return( visited )

        for edges in addList[vertex]:
            Q.insert(0, edges)

    return(visited)
