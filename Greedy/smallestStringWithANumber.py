'''
LC 1663. Smallest String With A Given Numeric Value
'''
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        result = ""
        i = n
        
        ALPHA_SIZE = 26
        
        while i > 0:
            #if all the next positions can be filled with 'z' then fill current position with 'a'
            if ALPHA_SIZE*(i-1) >= k-1:
                result +="a"
                k -= 1
            else:
                #even after filling all next positions with 'z' we need to fill this with some value greather than 'a'
                p = k - (i-1)*ALPHA_SIZE
                result += chr(ord('a') + (k - (i-1)*ALPHA_SIZE) - 1)
                k -= p
            
            i -= 1
            
        return result