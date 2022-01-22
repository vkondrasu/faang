from threading import Thread
from multiprocessing import Process
from multiprocessing.managers import BaseManager

import time
import multiprocessing

class SumUpClass:

    def __init__(self) -> None:
        self.counter = 0

    def add_integers(self, start, end):
        for i in range(start, end+1):
            self.counter += i
    
    def getCounter(self):
        return self.counter

def single_thread():
    obj = SumUpClass()
    start = time.time()
    obj.add_integers(1,30000000)
    end = time.time() - start
    print("Single thread took time: {} seconds and counter: {} ".format(end, obj.getCounter()))


def multiple_threads():
    obj1 = SumUpClass()
    obj2 = SumUpClass()
    start = time.time()

    t1 = Thread(target=obj1.add_integers, args=(1,15000000))
    t2 = Thread(target=obj2.add_integers, args=(15000001,30000000))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    combined_sum = obj1.counter + obj2.counter
    end = time.time() - start

    print("multiple threads took : {} seconds and summed to {}".format(end, combined_sum))

def single_process(obj, start, end):
    obj.add_integers(start, end)

def multiple_processes():
    BaseManager.register('SumUpClass', SumUpClass)
    manager = BaseManager(address=('127.0.0.1', 63333))
    manager.start()

    obj1 = manager.SumUpClass()
    obj2 = manager.SumUpClass()
    start = time.time()

    p1 = Process(target=single_process, args=(obj1, 1,15000000))
    p2 = Process(target=single_process, args=(obj2, 15000001,30000000))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    combined_sum = obj1.getCounter() + obj2.getCounter()
    end = time.time() - start
    print("multiple processes took : {} seconds and summed to {}".format(end, combined_sum))
    manager.shutdown()



if __name__ == "__main__":
    print("System has {0} CPUs".format(multiprocessing.cpu_count()))
    single_thread()
    multiple_threads()
    multiple_processes()
