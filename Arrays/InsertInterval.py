'''
LC 57. Insert Interval
'''

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start, new_end = newInterval
        idx, n = 0, len(intervals)
        
        output = []
        
        #if intervals are starting before this then don't do anything
        while idx < n and intervals[idx][0] < new_start:
            output.append(intervals[idx])
            idx += 1
        
        #if this is the first interval or start is after end then we can append
        if len(output) == 0 or output[-1][1] < new_start:
            output.append(newInterval)
        else: #it's overlapping with last interval
            output[-1][1] = max(output[-1][1], new_end)
         
        #for the rest of the intrevals check if they are ovelapping with previous
        while idx < n:
            start, end = intervals[idx]
            
            if output[-1][1] < start:
                output.append(intervals[idx])
            else:
                output[-1][1] = max(output[-1][1], end)
            
            idx += 1
            
        return output