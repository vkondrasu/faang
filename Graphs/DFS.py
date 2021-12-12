class DFSAlgo:
    def dfs(self, at, visited, g):
        if visited[at]:
            return
        visited[at] = True
        print(at)

        neighbours = g[at]

        for next in neighbours:
            self.dfs(next, visited, g)

    def traverseDFS(self, start_node, g):
        n = len(g)
        visited = [False]*n

        self.dfs(start_node, visited, g)


s = DFSAlgo()

s.traverseDFS(0, [[1,2,4],[0,2,3,7],[1,4,5],[4,7,6],[1,2,5],[3,2,6,],[7],[0]])