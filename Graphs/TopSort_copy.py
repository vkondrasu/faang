def topSort(graph):
    n = len(graph)
    visited = [False] * n
    ordering = [-1] * n

    i = n-1

    for at in range(n):
        if not visited[at]:
            visitedNodes = []
            dfs(at, visited, visitedNodes, graph)

            for nodeId in visitedNodes:
                ordering[i] = nodeId
                i = i-1

    return ordering

def dfs(at, visited, visitedNodes, graph):

    visited[at] = True

    for edge in graph[at]:
        if not visited[edge]:
            dfs(edge, visited, visitedNodes, graph)

    visitedNodes.append(at)


print( topSort( [[1,2],[2,3,4],[6],[2,4,5,6],[7],[7],[7],[]] ) )


"""
[[3],[3],[0,1],[6,7],[3,5],[9,10],[8],[8,9],[11],[11,12],[9],[],[]]
[[1,2],[2,3,4],[3,6],[4,5,6],[7],[7],[7],[]]
"""