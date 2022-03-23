'''
LC 125. Valid Palindrome
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphaNum(c):
            lower_alphabet_low = 97
            lower_alphabet_high = 122
            num_low = 48
            num_high = 57
            return (ord(c) >= lower_alphabet_low and ord(c) <= lower_alphabet_high) or (ord(c) >= num_low and ord(c) <= num_high)
        
        i = 0
        n = len(s)
        j = n-1
        s = s.lower()
        
        while i <= j:
            while i < j and not isAlphaNum(s[i]):
                i += 1
            while i < j and not isAlphaNum(s[j]):
                j -= 1
                
            if s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
            
        return True