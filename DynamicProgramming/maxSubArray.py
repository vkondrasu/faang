'''
LC 53. Maximum Subarray
'''
class Solution:
    def maxSubArray(self, nums) -> int:
        #take first element as cur and maxx
        cur, maxx = nums[0], nums[0]

        for num in nums[1:]:
            #either the number can be added to prev sum or number is a fresh start
            cur = max(num, cur+num)
            #keep track of maxx at each step
            maxx = max(maxx, cur)

        return maxx

s = Solution()

assert(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6)
assert(s.maxSubArray([-2,1,-3,4,-1,2,1,5,-5,4]) == 11)
assert(s.maxSubArray([1]) == 1)
assert(s.maxSubArray([5,4,-1,7,8]) == 23)
assert(s.maxSubArray([5,4,-1,-8,7,-8]) == 9)