'''
LC 881. Boats to Save People
'''
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        n = len(people)
        i, j, count = 0, n-1, 0
        
        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
            count += 1
        return count