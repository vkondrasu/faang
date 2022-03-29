'''
LC 287. Find the Duplicate Number
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        #repeated number can come any number of times
        #for that case it will not work
        #[2,2,2,2,2]
        n = len(nums)-1
        expected_sum = n* (n+1)//2
        summ = 0
        for n in nums:
            summ += n
            
        return (summ - expected_sum)
        '''
        #negative marking
        result = -1
        for n in nums:
            n = abs(n)
            if nums[n] < 0:
                result = n
                break
            else:
                nums[n] = -nums[n]
                
        for n in nums:
            if nums[n] < 0:
                nums[n] = -nums[n]
                
        return result