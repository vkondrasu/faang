'''
LC 74. Search a 2D Matrix
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        rows = len(matrix)
        cols = len(matrix[0])
        
        def binarySearch(row, start, end):
            l = start
            r = end
            
            while l <= r:
                mid = l + (r-l)//2
                if matrix[row][mid] == target:
                    return True
                if matrix[row][mid] < target:
                    l = mid+1
                else:
                    r = mid-1
                    
            return False
        
        for i in range(rows):
            if target >= matrix[i][0] and target <= matrix[i][cols-1]:
                return binarySearch(i,0,cols-1)
            
        return False
        '''
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        
        # binary search
        left, right = 0, m * n - 1
        while left <= right:
                pivot_idx = (left + right) // 2
                pivot_element = matrix[pivot_idx // n][pivot_idx % n]
                if target == pivot_element:
                    return True
                else:
                    if target < pivot_element:
                        right = pivot_idx - 1
                    else:
                        left = pivot_idx + 1
        return False