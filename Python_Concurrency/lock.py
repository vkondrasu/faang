from threading import Thread, current_thread
from threading import Lock
import random

shared = [1,2,3,4]
my_lock = Lock()

def updateState():
    for _ in range(10):
        print("{0} trying to acquire the lock".format(current_thread().getName()))
        my_lock.acquire()
        print("{0} acquired the lock".format(current_thread().getName()))

        shared[1] = random.randint(1, 24500)

        print("{0} about to release the lock".format(current_thread().getName()))
        my_lock.release()
        print("{0} released the lock".format(current_thread().getName()))


def readState():
    for _ in range(10):
        print("{0} trying to acquire the lock".format(current_thread().getName()))
        my_lock.acquire()
        print("{0} acquired the lock".format(current_thread().getName()))

        print("reading state: ", shared[1])

        print("{0} about to release the lock".format(current_thread().getName()))
        my_lock.release()
        print("{0} released the lock".format(current_thread().getName()))


if __name__ == "__main__":
    t1 = Thread(name="updater thread", target=updateState)
    t1.start()
    t2 = Thread(name="reader thread", target=readState)
    
    t2.start()

    t1.join()
    t2.join()