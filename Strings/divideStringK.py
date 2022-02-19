'''
LC 2138. Divide a String Into Groups of Size k
'''
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        start = 0
        
        result = []
        while start < n:
            if (start + k) > n:
                result.append(s[start: n]+ fill * (start+k-n))
            else:
                result.append(s[start: start+k])
                
            start += k
            
        return result