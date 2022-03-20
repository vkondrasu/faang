'''
LC 1007. Minimum Domino Rotations For Equal Row
'''
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        
        #the element has to be one of the element from 0th position of tops or bottom
        elements = set()
        elements.add(tops[0])
        elements.add(bottoms[0])
        
        #next positions has to be one of the elemets from previous set
        for i in range(1,n):
            elements = elements.intersection(set([tops[i], bottoms[i]]))
            
            #if no elements then we can't make it
            if len(elements) < 1:
                return -1
        #set contains only one element -- we need to find the freq of this element in tops and bottoms   
        element = list(elements)[0]
        
        counts = [0,0]
        for i in range(n):
            if tops[i] == element:
                counts[0] = counts[0]+1
            if bottoms[i] == element:
                counts[1] = counts[1]+1
        
        #rotate min of missing positions        
        return min(n-counts[0], n-counts[1])