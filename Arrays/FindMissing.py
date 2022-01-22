'''
448. Find All Numbers Disappeared in an Array
'''

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        hashSet = set(range(1, len(nums)+1))
        
        for num in nums:
            if num in hashSet:
                hashSet.remove(num)
                
        return list(hashSet)