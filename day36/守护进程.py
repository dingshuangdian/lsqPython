# 守护进程
# 子进程--》守护进程

import time
from multiprocessing import Process


def func():
    while True:
        time.sleep(0.5)
        print('alive')


def func2():
    print('in func2 start')
    time.sleep(8)
    print('in func2 finished')


if __name__ == '__main__':
    p = Process(target=func)
    p.daemon = True  # 设置子进程为守护进程
    p.start()
    Process(target=func2).start()
    i = 0

    while i < 5:
        print('I am a socket server!')
        time.sleep(1)
        i += 1

# 守护进程会随着主进程的代码执行完毕结束而结束
