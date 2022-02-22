'''
LC 1064. Fixed Point
'''
class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        l = 0
        r = len(arr)-1
        answer = -1
        
        while l <= r:
            mid = l + (r-l)//2
            
            if arr[mid] == mid:
                answer = mid
                r = mid-1
                
            elif arr[mid] < mid:
                l = mid+1
            else:
                r = mid-1
                
        return answer