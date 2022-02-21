'''
LC 169. Majority Element
'''
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mapp = Counter(nums)
        
        for num in mapp:
            if mapp[num] > len(nums)//2:
                return num