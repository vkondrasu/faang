'''
LC 155. Min Stack
'''
import math

class MinStack:
    '''
    uses the approach to store min at each element 
    so that all operations can be done O(1) time
    '''

    def __init__(self):
        self.arr = []
        self.min = math.inf
        

    def push(self, val: int) -> None:
        if val < self.min:
            self.min = val
        self.arr.append((val, self.min))
        

    def pop(self) -> None:
        self.arr.pop()
        if len(self.arr) > 0:
            self.min = self.arr[-1][1]
        else:
            self.min = math.inf
        

    def top(self) -> int:
        return self.arr[-1][0]
        

    def getMin(self) -> int:
        return self.arr[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()