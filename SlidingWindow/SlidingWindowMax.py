'''
LC 239. Sliding Window Maximum
'''
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r, n = 0, 0, len(nums)
        q = deque()
        output = []

        while r < n:
            #maintain q elements in decreasing order
            #such that we always have the current window max at the start q[0] of the q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r+1) >= k:
                output.append(nums[q[0]])
                l += 1

            r += 1

        return output