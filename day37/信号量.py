# 多进程中的组件

# 一套资源 同意时间  只能被n个人访问

# 某一段代码 同一时间  只能被n个进程执行

import time

import random

from multiprocessing import Process
from multiprocessing import Semaphore


# 多进程中的组件
# ktv
# 4个
# 一套资源  同一时间 只能被n个人访问
# 某一段代码 同一时间 只能被n个进程执行


# sem = Semaphore(4)
# sem.acquire()
# print('拿到第一把钥匙')
# sem.acquire()
# print('拿到第二把钥匙')
# sem.acquire()
# print('拿到第三把钥匙')
# sem.acquire()
# print('拿到第四把钥匙')
# sem.acquire()
# print('拿到第五把钥匙')
def ktv(i, sem):
    sem.acquire()  # 获取钥匙
    print('%s走进ktv' % i)
    time.sleep(random.randint(1, 5))
    print('%s走出ktv' % i)
    sem.release()


if __name__ == '__main__':
    sem = Semaphore(4)
    for i in range(20):
        p = Process(target=ktv, args=(i, sem))
        p.start()
