'''
LC 560. Subarray Sum Equals K
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        summ = 0
        
        mapp = {}
        mapp[0] = 1
        
        for num in nums:
            summ += num
            
            if summ - k in mapp:
                count += mapp.get(summ-k)
            
            mapp[summ] = mapp.get(summ, 0) + 1
            
        return count