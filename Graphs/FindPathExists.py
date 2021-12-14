class Solution:
    def validPath(self, n: int, edges, start: int, end: int) -> bool:
        
        if start == end:
            return True
        
        if len(edges) < 1:
            return False
        
        self.graph = dict()
        self.found = False
        
        for edge in edges:
            if edge[0] in self.graph:
                self.graph[edge[0]] = self.graph[edge[0]] + [edge[1]]
            else:
                self.graph[edge[0]] = [edge[1]]
                
            if edge[1] in self.graph:
                self.graph[edge[1]] = self.graph[edge[1]] + [edge[0]]
            else:
                self.graph[edge[1]] = [edge[0]]
                
        self.visited = [False] * n   
        
        #print( self.graph )
                
        self.dfs(start, end)
        
        return self.found
    
    def dfs(self, start, end):
        
        self.visited[start] = True
        """ Does this make any sense """
        if self.found:
            return
        for edge in self.graph[start]:
            if edge == end:
                self.found = True
                break
            if not self.visited[edge]:
                self.dfs(edge, end)
            
        
s = Solution()
answer = s.validPath(50,
[[31,5],[10,46],[19,31],[5,1],[31,28],[28,29],[8,26],[13,23],[16,34],[30,1],[16,18],[33,46],[27,35],[2,25],[49,33],[44,19],[22,26],[30,13],[27,12],[8,16],[42,13],[18,3],[21,20],[2,17],[5,48],[41,37],[39,37],[2,11],[20,26],[19,43],[45,7],[0,21],[44,23],[2,39],[27,36],[41,48],[17,42],[40,32],[2,28],[35,38],[3,9],[41,30],[5,11],[24,22],[39,5],[40,31],[18,35],[23,39],[20,24],[45,12]]
,29,
46)

print(answer)

