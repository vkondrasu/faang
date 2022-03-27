'''
LC 1337. The K Weakest Rows in a Matrix
'''
from unittest import result


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        new_mat = []
        n = len(mat)
        for i in range(n):
            #summ = [sum(x) for x in mat[i]]
            new_mat.append((sum(mat[i]), i))
            
        new_mat = sorted(new_mat)
        result = []
        for summ, i in new_mat[:k]:
            result.append(i)
            
        return result

    def kWeakestRowsVerticalIteration(self, mat: List[List[int]], k: int) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        
        result = []

        for i in range(rows):
            if mat[i][0] == 0 and len(result) < k:
                result.append(i)
        
        if len(result) == k:
            return result
        done = False
        
        for c in range(1, cols):
            if done: break
            for r in range(rows):
                if len(result) < k and mat[r][c] == 0 and mat[r][c-1] != 0:
                    result.append(r)
                elif len(result) == k:
                    done = True
                    break
        i = 0
        while len(result) < k:
            if mat[i][-1] == 1:
                result.append(i)
            i += 1
            
        return result