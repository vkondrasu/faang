from threading import *
import time

def thread_A(lock1, lock2):
    lock1.acquire()
    print("{0} acquired lock1".format(current_thread().getName()))
    time.sleep(1)
    lock2.acquire()
    print("{0} acquired both locks".format(current_thread().getName()))


def thread_B(lock1, lock2):
    lock2.acquire()
    print("{0} acquired lock2".format(current_thread().getName()))
    time.sleep(1)
    lock1.acquire()
    print("{0} acquired both locks".format(current_thread().getName()))


if __name__ == "__main__":

    lock1 = Lock()
    lock2 = Lock()

    Thread(target=thread_A, args=(lock1, lock2)).start()
    Thread(target=thread_B, args=(lock1, lock2)).start()