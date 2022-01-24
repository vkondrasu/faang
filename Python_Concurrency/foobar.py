'''
LC 1115. Print FooBar Alternately
'''

from threading import *

foo_count = 0
bar_count = 0

def printFoo():
    global foo_count
    foo_count += 1
    print("foo", end="")

def printBar():
    global bar_count
    bar_count += 1
    print("bar", end="")

class FooBar:
    def __init__(self, n):
        self.n = n
        self.cond_var = Condition()
        self.fooTime = True


    def foo(self):
        
        for i in range(self.n):
            self.cond_var.acquire()
            while not self.fooTime:
                self.cond_var.wait()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.fooTime = False
            self.cond_var.notifyAll()
            self.cond_var.release()

        print(foo_count)


    def bar(self):
        
        for i in range(self.n):
            self.cond_var.acquire()
            while self.fooTime:
                self.cond_var.wait()
            printBar()
            #self.cond_var.acquire()
            self.fooTime = True
            self.cond_var.notifyAll()
            self.cond_var.release()

        print(bar_count)


#if __name__ == "__main":
f = FooBar(500000)

foo_thread = Thread(target=f.foo)
foo_thread.start()

foo_thread1 = Thread(target=f.foo)
foo_thread1.start()

bar_thread = Thread(target=f.bar)
bar_thread.start()

bar_thread1 = Thread(target=f.bar)
bar_thread1.start()

foo_thread.join()
bar_thread.join()

