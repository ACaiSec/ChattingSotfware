# coding: utf-8
from threading import Timer
import time


# 进测试模块功能

def fun():
    while True:
        print("hello, world")
        time.sleep(2)

if __name__=='__main__':
    t = Timer(5.0, fun)
    t.start() # 5秒后, "hello, world"将被打印
    time.sleep(15)
    t.cancel()
