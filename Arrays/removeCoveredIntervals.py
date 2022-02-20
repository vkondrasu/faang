'''
LC 1288. Remove Covered Intervals
'''
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervalas = sorted(intervals, key = lambda i : [i[0], -i[1]] )
        #intervals.sort()
        removed_count = 0
        last_interval = sorted_intervalas[0]
        
        for i in range(1,len(sorted_intervalas)):
            if sorted_intervalas[i][0] == last_interval[0] or sorted_intervalas[i][1] <= last_interval[1]:
                removed_count += 1
            else:
                last_interval = sorted_intervalas[i]
        
        return len(intervals) - removed_count