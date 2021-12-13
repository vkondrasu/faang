""""
This implementation has some fault
need to fix that
"""

class TopologicalOrder:
    def dfs(self,i, visited, orderList, inPos, g):
        
        visited[i] = True

        for next in g[i]:
            if not visited[i]:
                inPos = self.dfs(next, visited, orderList, inPos, g)

        orderList[inPos] = i
        return inPos-1
        

    def getTopologicalOrder(self, g):
        n = len(g)
        visited = [False]*n

        orderList = [-1]*n

        inPos = n-1

        for i in range(n):
            if not visited[i]:
                inPos = self.dfs(i, visited, orderList, inPos, g)

        print(orderList)


s = TopologicalOrder()
s.getTopologicalOrder( [[3],[3],[0,1],[6,7],[3,5],[9,10],[8],[8,9],[11],[11,12],[9],[],[]] )



"""
[
    [3],
    [3],
    [0,1],
    [6,7],
    [3,5],
    [9,10],
    [8],
    [8,9],
    [11],
    [11,12],
    [9],
    [],
    []
]
"""