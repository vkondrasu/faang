'''
LC 1101. The Earliest Moment When Everyone Become Friends
'''
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        mapp = {}
        parent = [-1]*n
        
        logs.sort()
        #sorted(logs, key = lambda x : x[0])
        #print(logs)
        
        for log in logs:
            if parent[log[1]] == -1 and parent[log[2]] == -1:
                parent[log[1]] = log[1]
                parent[log[2]] = log[1]
                
                mapp[log[1]] = set([log[1], log[2]])
                if len(mapp[log[1]]) == n:
                    return log[0]
            elif parent[log[1]] != -1 and parent[log[2]] != -1:
                if parent[log[1]] == parent[log[2]]:
                    continue
                todel = parent[log[2]]
                for x in mapp[parent[log[2]]]:
                    parent[x] = parent[log[1]]
                    mapp[parent[log[1]]].add(x)
                    
                del mapp[todel]
                if len(mapp[parent[log[1]]]) == n:
                    return log[0]
            else:
                if parent[log[1]] != -1:
                    parent[log[2]] = parent[log[1]]
                    mapp[parent[log[1]]].add(log[2])
                    if len(mapp[parent[log[1]]]) == n:
                        return log[0]
                else:
                    parent[log[1]] = parent[log[2]]
                    mapp[parent[log[2]]].add(log[1])
                    if len(mapp[parent[log[2]]]) == n:
                        return log[0]
                
        return -1
        