class Solution:
    
    def arraySign(self, nums: List[int]) -> int:
        
        summ = 1
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                summ *= -1
            
        return summ