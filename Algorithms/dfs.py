def DFS(first, finish, addlist):
      """Performs a Depth-First-Search on the graph structure, outputs
      list of vertices"""

      S = [first]
      visited = []

      while len(S) > 0:
          vertex = S.pop()

          if vertex not in visited:
              visited.append(vertex)
              if finish in visited:
                  return( visited )
              for edges in addlist[vertex]:
                  S.append(edges)

      return( visited )
