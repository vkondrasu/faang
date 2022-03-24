'''
LC 8. String to Integer (atoi)
'''
class Solution:
    def myAtoi(self, s: str) -> int:
        #remove leading and trailing spaces
        s = s.strip()
        n = len(s) 
        #if empty string return 0
        if n== 0:
            return 0
        
        i = 0
        factor = 1
        
        #not starting with number or sign -- then return 0
        if i < n and s[i] not in ['+','-','0','1','2','3','4','5','6','7','8','9']:
            return 0
        #if sign, capture in factor   
        if i < n and (s[i] == '-' or s[i] == '+'):
            if s[i] == '-':
                factor = -1
            i +=1
        #ignore leading 0s    
        while i < n and s[i] == '0':
            i += 1
            
        result = 0
        
        #read numbers 
        while i < n and s[i] in ['0','1','2','3','4','5','6','7','8','9']:
            result = result * 10 + ord(s[i]) - ord('0')
            i += 1
            
        result *= factor
            
        return  max(result, -2**31) if result < 0 else  min(result, 2 ** 31 - 1)