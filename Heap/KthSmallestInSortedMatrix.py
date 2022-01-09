'''
LC 378

Another approach using the Binary search -- need to revist this again

'''


import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        minHeap = []
        
        rows, cols = len(matrix), len(matrix[0])
        
        #keep firstrow in the heap
        for i in range(cols):
            minHeap.append((matrix[0][i], [0,i]))
            
        heapq.heapify(minHeap)
        
        temp  = k

        #remove k-1 elements from the heap
        #each time we remove a element add the next bigger element in that column -- so that we maintain the order in the minHeap
        
        while temp > 1:
            cur, location = minHeap[0]
            heapq.heappop(minHeap)
            if location[0]+1 < rows:
                heapq.heappush(minHeap, (matrix[location[0]+1][location[1]],[location[0]+1, location[1]] ) )
            temp -= 1
            
        return minHeap[0][0]