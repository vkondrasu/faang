import heapq

#1.
#construct an empty MinHeap
minHeap = []
heapq.heapify(minHeap)

#2.
#construct an empty MaxHeap
#There are no internal functions to construct max heap

#3.
#Construct a heap (min) with initial values
minHeap = [3,1,2]
heapq.heapify(minHeap)
print(minHeap)

#4.
#Since no internal functions to construct MaxHeap we can use a trick
#multiply element with -1 and construct min heap, while retriving do * -1 to get actual element

maxHeap = [1,2,3]
maxHeap = [-x for x in maxHeap]
heapq.heapify(maxHeap)
print([-x for x in maxHeap])

#5.
#inserting an elment into the heaps
heapq.heappush(minHeap, 5)
heapq.heappush(maxHeap, 5 * -1)
print(minHeap)
print([-x for x in maxHeap])

#6.
#Getting top of the heap
print(minHeap[0])
print(maxHeap[0] * -1)

#7.
#Delete top of the heap
heapq.heappop(minHeap)
heapq.heappop(maxHeap)

print(minHeap)
print([-x for x in maxHeap])

#8
#length of heap
print(len(minHeap))
print(len(maxHeap))


