'''
LC 1337. The K Weakest Rows in a Matrix
'''
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