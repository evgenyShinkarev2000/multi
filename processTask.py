import concurrent.futures
import multiprocessing
from hashlib import md5
from random import choice
import time

startTime = time.time()
maxWorkers = 16


def event(s, h):
    print(s, h)
    global generalMoney
    global startTime
    generalMoney.value -= 1

    if generalMoney.value <= 0:
        print(f"time {round(time.time() - startTime)}s process {maxWorkers}")


def miner():
    while True:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("00000"):
            event(s, h)


def set_global(args):
    global generalMoney
    generalMoney = args


def mining():
    if __name__ == '__main__':
        money = multiprocessing.Value("i", 3)
        with concurrent.futures.ProcessPoolExecutor(max_workers=maxWorkers, initializer=set_global, initargs=(money,)) as executor:
            futures = []
            for i in range(0, maxWorkers):
                futures.append(executor.submit(miner))

mining()
