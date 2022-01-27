'''
LC 200. Number of Islands
'''

from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            dr = [-1,0,0,+1]
            dc = [0,+1,-1,0]
            
            visited.add((r,c))
            while q:
                row, col = q.popleft()
                for i in range(4):
                    nr = row+dr[i]
                    nc = col+dc[i]
                    if (nr > -1 and nr < rows) and ( nc > -1 and nc < cols ) and (nr, nc) not in visited and grid[nr][nc] == "1":
                        q.append((nr,nc))
                        visited.add((nr,nc))
                    
                
                
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
                    
        return islands