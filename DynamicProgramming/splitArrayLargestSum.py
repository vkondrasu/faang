'''
LC 410. Split Array Largest Sum
'''
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        #divide array in such a way that subarray sum won't exceed a given value 'x'
        def min_subarrays_required(x):
            cur_sum = 0
            splits_required = 0
            
            for num in nums:
                if cur_sum + num <= x:
                    cur_sum += num
                else:
                    splits_required += 1
                    cur_sum = num
                    
            return splits_required + 1
        
        #we can't do a min of max >= max(nums), as we can't divide the max(nums) further
        left = max(nums)
        #max sum would be sum of all the elements
        right = sum(nums)
        
        while left <= right:
            max_sum_allowed = (left+right)//2
            
            #if we are not able to get 'm' partitions then we can reduce the partition sum further
            #if we get exactly 'm' then try reducing the partition sum further
            if min_subarrays_required(max_sum_allowed) <= m:
                right = max_sum_allowed - 1
                minimum_largest_split_sum = max_sum_allowed
            else: # we got more than required partitions, increase the maxsum of partition
                left = max_sum_allowed + 1
                
        return minimum_largest_split_sum