'''
LC 402. Remove K Digits
'''

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        '''
        BFS time limit exceeded
        BFS + visited -- memory limit exceeded
        '''
        
        if k == 0:
            return num
        
        if k == len(num):
            return "0"
        
        visited = set()
        q = deque()
        minn = int(num)
        n = len(num)
        for i in range(n):
            temp = num[0:i] + num[i+1:n]
            q.append(temp)
            visited.add(temp)
            
        j = 0
        
        while q and j < k:
            size = len(q)
            for _ in range(size):
                num = q.popleft()
                minn = min(minn, int(num))
                n = len(num)
                for i in range(n):
                    temp = num[0:i] + num[i+1:n]
                    if temp not in visited:
                        q.append(temp)
                        visited.add(temp)
            
            j += 1
            
        return str(minn)
        