class ConnectedComponents:
    def isConnected(self,a, b, comp):
        return comp[a] == comp[b]

    def markConnected(self, at, comp_id, comp, g):
        if comp[at] == comp_id:
            return
        comp[at] = comp_id

        for next in g[at]:
            self.markConnected(next, comp_id, comp, g)


    def connect(self,start_node, g):
        n = len(g)
        comp = [-1]*n

        for i in range(n):
            if comp[i] == -1:
                self.markConnected(i,i,comp,g)

        for i in range(n):
            print(comp[i])

s = ConnectedComponents()
s.connect(0, [[8],[5],[9],[9],[0],[16,17],[11],[6],[4,14],[15],[],[7],[],[0],[0,13],[2,10],[],[]])



"""
[
    [8],
    [5],
    [9],
    [9],
    [0],
    [16,17],
    [11],
    [6],
    [4,14],
    [15],
    [],
    [7],
    [],
    [0],
    [0,13],
    [2,10],
    [],
    []
]

"""