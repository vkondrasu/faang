'''
LC 1114. Print in Order
'''

from threading import *

class Foo:
    def __init__(self):
        self.printFirst = True
        self.printSecond = False
        self.printThird = False
        self.cond_var = Condition()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        self.cond_var.acquire()
        while not self.printFirst:
            self.cond_var.wait()
        self.cond_var.release()
        printFirst()
        self.cond_var.acquire()
        self.printSecond = True
        self.cond_var.notifyAll()
        self.cond_var.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        self.cond_var.acquire()
        while not self.printSecond:
            self.cond_var.wait()
        self.cond_var.release()
        printSecond()
        self.cond_var.acquire()
        self.printThird = True
        self.cond_var.notifyAll()
        self.cond_var.release()
        


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        self.cond_var.acquire()
        while not self.printThird:
            self.cond_var.wait()
        self.cond_var.release()
        printThird()