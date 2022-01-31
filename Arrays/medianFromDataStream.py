'''
LC 295. Find Median from Data Stream
'''

class MedianFinder:

    def __init__(self):
        self.lst = []
        self.count = 0
        self.median = 0
        
    def addNum(self, num: int) -> None:
        #insert into sorted array
        l = 0
        r = self.count - 1
        while l <= r:
            m = l +(r-l)//2
            if self.lst[m] == num:
                self.lst.insert(m, num)
                self.count += 1
                return
            elif num > self.lst[m]:
                l = m+1
            else:
                r = m-1
                
        self.lst.insert(l, num)
        self.count += 1
        

    def findMedian(self) -> float:
        m = self.count // 2
        if self.count % 2 == 0:
            self.median = ( self.lst[m-1] + self.lst[m] ) /2
        else:
            self.median = self.lst[m]
        return self.median
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()