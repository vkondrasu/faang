'''
LC 410 with m = 2
'''
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        summ = 0
        n = len(nums)
        
        for num in nums:
            summ += num
            
        lsum = nums[0]
        rsum = summ - lsum
        
        minSum = max(lsum, rsum)
        
        for i in range(1,n):
            lsum += nums[i]
            rsum -= nums[i]
            
            minSum = min(minSum, max(lsum, rsum))
            
        return minSum