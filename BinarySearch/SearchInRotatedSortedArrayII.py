'''
LC 81. Search in Rotated Sorted Array II
'''
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums)-1
        
        while l <= r:
            while l < r and nums[l] == nums[l+1]:
                l += 1
            while l < r and nums[r] == nums[r-1]:
                r -= 1
            
            m = l + (r-l)//2
            
            if nums[m] == target:
                return True
            
            if nums[l] <= nums[m]:
                if target >= nums[l] and target < nums[m]:
                    r = m-1
                else:
                    l = m+1
            else:
                if target <= nums[r] and target > nums[m]:
                    l = m+1
                else:
                    r = m-1
                    
        return False