# Create by dingshuangdian


# 多个进程可以同时执行  并发
# 我们现在写的一个py文件就自己一个进程  同步执行代码
# 并发效果:
    # 在我们自己的一个py文件里 启动多个进程
    # 多个进程之间 - 操作系统
# 如何在自己的py文件里 启动一个进程
import os
import time
from multiprocessing import Process
def func():
    print('heiheihei')
    time.sleep(1)
    print(os.getpid())
    print('hahaha')

if __name__ == '__main__':
    print('**',os.getpid())
    p = Process(target=func)
    p.start()    #启动一个进程
    print('**',os.getpid())