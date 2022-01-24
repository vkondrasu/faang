'''
LC 520. Detect Capital
'''

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        def isAllCapital(word):
            result = True
            for c in word:
                asc = ord(c)
                if asc < 65 or asc > 90:
                    return False
            return result
        
        def isAllSmall(word):
            result = True
            for c in word:
                asc = ord(c)
                if asc < 97 or asc > 122:
                    return False
            return result
        
        return isAllCapital(word) or (isAllCapital(word[0]) and isAllSmall(word[1:])) or isAllSmall(word)
        