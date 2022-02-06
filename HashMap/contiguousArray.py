'''
LC 525. Contiguous Array
'''

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mapp = {}
        #mapp[0] = [0,0]
        count = 0
        max_len = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
                
            if count == 0:
                max_len = i+1
            else:
                
                if count in mapp:
                    mapp[count][1] = i
                else:
                    mapp[count] = [i,i]
            
                max_len = max(max_len, i - mapp[count][0])
            
        return max_len