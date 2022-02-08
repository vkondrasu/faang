'''
LC 258. Add Digits
'''

class Solution:
    def addDigits(self, num: int) -> int:
        
        while num > 9:
            temp = num
            num = 0
            while temp > 0:
                num += temp%10
                temp //= 10
                
        return num