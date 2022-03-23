'''
LC 991. Broken Calculator
'''
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        '''
        #This BFS approach exceeded time limit for s, t = 1024, 1
        q = deque()
        q.append([startValue,0])
        visited = set()
        visited.add(startValue)
        
        while q:
            size = len(q)
            for i in range(size):
                cur,count = q.popleft()
                if cur*2 == target:
                    return count+1
                elif cur*2 not in visited:
                    q.append([cur*2, count+1])
                    
                if cur-1 == target:
                    return count+1
                elif cur-1 not in visited:
                    q.append([cur-1, count+1])
                    
                    
        return -1
        '''
        ans = 0
        
        while target > startValue:
            ans += 1
            if target%2:
                target += 1
            else:
                target //= 2
        #If target is less than startValue we have no option but to deduct 1 at each step
        return ans+startValue-target