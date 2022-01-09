import heapq

class Solution:
    #space of 1000001 -- leet code mentioned intervals start/end max value as this -- obviously a lot of memory even for a smaller problem
    #second issue of travesrsing till the max_interval
    #Space is constant - but huge 10000001
    #Time complexity is O(max_interval)
    def minMeetingRoomsNaive(self, intervals: List[List[int]]) -> int:
        meetings = [0] * 10000001
        
        max_interval = 0
        
        for interval in intervals:
            max_interval = max(max_interval, interval[1])
            meetings[interval[0]] += 1
            meetings[interval[1]] -= 1
        
        max_count = 0
        count = 0
        
        for i in range(max_interval):
            count +=  meetings[i]
            max_count = max(count, max_count)
            
        return max_count

    #using heap
    #sort the input list by starting time
    #maintain a min Heap of ending times
    # when a new meeting comes if the top of the MinHeap is <= start -- then we can re-use that meeting room : pop and push incoming end time
    # if top of the heap end time > start time of incoming request -- no other meeting going to be free -- do push
    # Each time keep track of len(maxHeap) -- maximum length of heap at any time is the max meeting rooms required
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[0])
        
        minHeap = []
        
        heapq.heappush(minHeap, intervals[0][1])
        max_count = 1
        
        for i in range(1, len(intervals)):
            interval = intervals[i]
            
            if interval[0] >= minHeap[0]:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, interval[1])
            else:
                heapq.heappush(minHeap, interval[1])
                
            max_count = max(max_count, len(minHeap))
            
        return max_count
