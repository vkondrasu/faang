from threading import *

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.printZero = True
        self.printOdd = False
        self.printEven = False
        self.cond_var = Condition()
        
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self) -> None:
        for i in range(1,self.n+1):
            self.cond_var.acquire()
            while not self.printZero:
                self.cond_var.wait()
                
            print("0", end="")
            
            self.printZero = False
            if i % 2 == 0:
                self.printEven = True
            else:
                self.printOdd = True
                
            self.cond_var.notifyAll()
            self.cond_var.release()
        
        
        
    def even(self) -> None:
        for i in range(1,self.n+1):
            if i %2 == 0:
                self.cond_var.acquire()
                while not self.printEven:
                    self.cond_var.wait()
                print(i, end="")
                
                self.printZero = True
                self.printEven = False
                self.cond_var.notifyAll()
                self.cond_var.release()
                
        
        
        
    def odd(self) -> None:
        for i in range(1,self.n+1):
            if i %2 == 1:
                self.cond_var.acquire()
                while not self.printOdd:
                    self.cond_var.wait()
                
                print(i, end="")
                
                self.printZero = True
                self.printOdd = False
                self.cond_var.notifyAll()
                self.cond_var.release()


z = ZeroEvenOdd(50)

zero_thread = Thread(target=z.zero)
zero_thread.start()

odd_thread = Thread(target=z.odd)
odd_thread.start()

even_thread = Thread(target=z.even)
even_thread.start()

zero_thread.join()
odd_thread.join()
even_thread.join()

print()
        
        