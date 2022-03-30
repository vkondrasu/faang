'''
LC 202. Happy Number
'''
class Solution:
    def isHappy(self, n: int) -> bool:
        hashset = set()
        while True:
            if n == 1:
                return True
            
            if n in hashset:
                return False
            hashset.add(n)
            temp = 0
            while n > 0:
                temp += (n%10)**2
                n = n//10
            n = temp