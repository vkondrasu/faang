from threading import Thread
from threading import Lock
import random
import time

rand_int = 0
lock = Lock()

def updater():
    global rand_int
    global lock
    while 1:
        with lock:
            rand_int = random.randint(1,9)

def printer():
    global rand_int
    global lock
    while 1:
        with lock:
            if rand_int % 5 == 0:
                if rand_int % 5 != 0:
                    print(rand_int)

if __name__ == "__main__":
    Thread(target=updater, daemon=True).start()
    Thread(target=printer, daemon=True).start()

    time.sleep(5)