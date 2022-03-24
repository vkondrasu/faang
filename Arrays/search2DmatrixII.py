'''
LC 240. Search a 2D Matrix II
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        
        r = 0
        c = cols-1
        
        while r > -1 and r < rows and c > -1 and c < cols:
            if matrix[r][c] == target:
                return True
            if matrix[r][c] < target:
                r += 1
            else:
                c -= 1
                
        return False