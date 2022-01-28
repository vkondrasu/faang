'''
LC 621. Task Scheduler
'''
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mapp = {}
        for task in tasks:
            mapp[task] = mapp.get(task, 0) + 1
            
        minHeap = []
        for k,v in mapp.items():
            minHeap.append((v*-1,k))
            
        heapq.heapify(minHeap)
        
        waiting_q = deque()
        time = 0
        while waiting_q or minHeap:
            time += 1
            if minHeap:
                time_left, job = heapq.heappop(minHeap)
            
                if time_left + 1 < 0:
                    waiting_q.append([time+n,(time_left+1,job)])
            if waiting_q and waiting_q[0][0] <= time:
                item = waiting_q.popleft()
                heapq.heappush(minHeap, item[1])
                
        return time
            
        