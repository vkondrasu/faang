class Solution:
        
    def countComponents(self, n, graph):
        self.component = [-1]*n
        self.count = 0
        self.graph = graph
        #print(edges)
        
        for i in range(n):
            if self.component[i] == -1:
                self.count += 1
                self.dfs(i, i)
                
        return self.count
                
    def dfs(self, at, comp_id):
        if self.component[at] == comp_id:
            return
        
        self.component[at] = comp_id
        
        for edge in self.graph[at]:
            self.dfs(edge, comp_id)


s = Solution()
print( s.countComponents(5, [[1,2],[0,2],[1,3],[2,4],[3]]) )