'''
LC 941. Valid Mountain Array
'''

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        count = 0
        n = len(arr)
        i = 0
        
        #walk up
        while i < n-1 and arr[i] < arr[i+1]:
            i += 1
            
        if i == 0 or i == n-1:
            return False
        #walk down
        while i < n-1 and arr[i] > arr[i+1]:
            i += 1
            
        return i == n-1
        