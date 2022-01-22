'''
LC 78 Subsets
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        
        for x in nums:
            size = len(result)
            cur = []
            for i in range(size):
                temp = result[i] + [x]
                cur.append( temp )
                
            result.extend(cur)
            
            
        return result