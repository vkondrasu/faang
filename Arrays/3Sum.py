'''
LC 15. 3Sum
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        
        def find2Sum(target, start, end):
            result = []
            while start < end:
                summ = nums[start] + nums[end]
                if summ == target:
                    #checking for duplicates here is less costly
                    if [nums[start], nums[end]] not in result:#eleminate duplicates
                        result.append([nums[start], nums[end]])
                    start += 1
                    end -= 1
                elif summ < target:
                    start += 1
                else:
                    end -= 1
            return result
        
        result = []
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]: #if consequtive elements are same we don't need to find the 2 sum again, we already found them
                continue
            twosum = find2Sum(-nums[i], i+1, n-1)
            if len(twosum) > 0:
                for temp in twosum:
                    result.append([nums[i], temp[0], temp[1]])
                
        return result
