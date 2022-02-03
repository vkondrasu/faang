'''
LC 165. Compare Version Numbers
'''
class Solution:
    #additional space
    def compareVersion(self, version1: str, version2: str) -> int:
        version1_s = version1.split(".")
        version2_s = version2.split(".")
        
        if len(version1_s) < len(version2_s):
            version1_s.extend(["0"]*(len(version2_s) - len(version1_s)))
        elif len(version1_s) > len(version2_s):
            version2_s.extend(["0"]*(len(version1_s) - len(version2_s)))
          
        result = 0
        for i in range(len(version1_s)):
            v1 = int(version1_s[i])
            v2 = int(version2_s[i])
            if v1 == v2:
                continue
            if v1 < v2:
                return -1
            else:
                return 1
        return result

    #space optimized
    def get_next_chunk(self, version: str, n: int, p: int) -> List[int]:
        # if pointer is set to the end of string
        # return 0
        if p > n - 1:
            return 0, p
        
        # find the end of chunk
        p_end = p
        while p_end < n and version[p_end] != '.':
            p_end += 1
        # retrieve the chunk
        i = int(version[p:p_end]) if p_end != n - 1 else int(version[p:n])
        # find the beginning of next chunk
        p = p_end + 1
        
        return i, p
        
    def compareVersionB(self, version1: str, version2: str) -> int:
        p1 = p2 = 0
        n1, n2 = len(version1), len(version2)
        
        # compare versions
        while p1 < n1 or p2 < n2:
            i1, p1 = self.get_next_chunk(version1, n1, p1)
            i2, p2 = self.get_next_chunk(version2, n2, p2)            
            if i1 != i2:
                return 1 if i1 > i2 else -1
        
        # the versions are equal
        return 0    
        