# Create by dingshuangdian

import os
import time
from multiprocessing import Process


def func(args, args2):
    print(args, args2)
    time.sleep(3)
    print('子进程:', os.getpid())
    print('子进程的父进程:', os.getpid())
    print(123456)


if __name__ == '__main__':  # windows系统需要
    p = Process(target=func, args=('参数', '参数2'))  # 注册

    # p是一个进程对象，还没有启动
    p.start()  # 开启了一个子进程
    print('*' * 10)
    print('父进程：', os.getpid())  # 查看当前进程的进程号
    print('父进程的父进程:', os.getppid())  # 查看当前进程的父进程

# 进程的生命周期
# 主进程
# 子进程
# 开启了子进程的主进程
# 主进程自己的代码如果长，等待自己的代码执行结束
# 子进程的执行时间长，主进程会在主进程代码执行完毕之后等待子进程执行完毕之后  主进程才结束
