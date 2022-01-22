from threading import Thread
from threading import Lock
import sys


class Counter:
    def __init__(self) -> None:
        self.count = 0
        self.lock = Lock()

    def increment(self):
        for _ in range(100000):
            self.lock.acquire()
            self.count += 1
            self.lock.release()

def multi_threading():

    num_of_threads = 5

    threads = [0] * num_of_threads

    counter = Counter()

    for i in range(num_of_threads):
        threads[i] = Thread(target=counter.increment)

    for i in range(num_of_threads):
        threads[i].start()

    for i in range(num_of_threads):
        threads[i].join()

    if counter.count != 500000:
        print(" count = {0}".format(counter.count), flush=True)
    else:
        print(" count = 50,000 - Try re-running the program.")


if __name__ == "__main__":
    multi_threading()

    