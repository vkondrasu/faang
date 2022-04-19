'''
LC 9. Palindrome Number
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        rev = 0
        n = x
        while n > 0:
            rev = (rev*10) + n%10
            n //= 10
            
        return rev == x