'''
LC 763. Partition Labels
'''
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mapp = {}
        for i in range(len(s)):
            if s[i] in mapp:
                mapp[s[i]][1] = i
            else:
                mapp[s[i]] = [i,i]
                
        #print(mapp.values())
        
        def mergeIntervals(intervals):
            #mapp.values()
            #print(intervals)
            result = [intervals[0]]
            
            for i in range(1, len(intervals)):
                interval = intervals[i]
                start, end = result[len(result)-1]
                if interval[0] > start and interval[0] < end:
                    result[len(result)-1][0] = min(start, interval[0])
                    result[len(result)-1][1] = max(end, interval[1])
                else:
                    result.append(interval)
                    
            return result
            
                
        result = mergeIntervals(list(mapp.values()))
        return [end-start+1 for start, end in result]

    def partitionLabelsEnumerate(self, S):
        last = {c: i for i, c in enumerate(S)}
        
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
            
        return ans
        