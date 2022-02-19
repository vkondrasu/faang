'''
LC 1160. Find Words That Can Be Formed by Characters
'''

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        resource = [0]*26
        for char in chars:
            resource[ord(char) - ord('a')] += 1
        
        result = 0
        for word in words:
            temp = resource.copy()
            possible = True
            for char in word:
                if temp[ord(char) - ord('a')] == 0:
                    possible = False
                    break
                else:
                    temp[ord(char) - ord('a')] -= 1
                    
            if possible:
                result += len(word)
                
        return result