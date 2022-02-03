'''
LC 7. Reverse Integer
'''
class Solution:
    def reverse(self, x: int) -> int:
        max_limit = 2147483647
        min_limit = -2147483648
        rev = 0
        factor = 1 if x >= 0 else -1
        x = abs(x)
        while x > 0:
            rev = rev*10 + x%10
            x //= 10
            if rev * factor > max_limit or rev*factor < min_limit:
                return 0
            
        return rev*factor