#coding: utf-8

from time import time,sleep

def dec(func):
    def f2():
        start_time = time()
        func()
        print(time() - start_time)
    return f2

@dec
def f1():
    sleep(1)

f1()
