'''
LC 695. Max Area of Island
'''
from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0
        
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            dr = [-1,0,0,+1]
            dc = [0,+1,-1,0]
            area = 0
            
            visited.add((r,c))
            while q:
                row, col = q.popleft()
                area += 1
                for i in range(4):
                    nr = row+dr[i]
                    nc = col+dc[i]
                    if (nr > -1 and nr < rows) and ( nc > -1 and nc < cols ) and (nr, nc) not in visited and grid[nr][nc] == 1:
                        q.append((nr,nc))
                        #area += 1
                        visited.add((nr,nc))
                    
            return area
                
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = bfs(r,c)
                    max_area = max(max_area, area)
                    
        return max_area
        