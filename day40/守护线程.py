import time
from threading import Thread
def func1():
    while True:
        print('*'*10)
        time.sleep(1)
def func2():
    print('in func2')
    time.sleep(5)

t = Thread(target=func1,)
t.daemon = True
t.start()
t2 = Thread(target=func2,)
t2.start()
t2.join()
print('主线程')

# 守护进程随着主进程代码的执行结束而结束
# 守护线程会在主线程结束之后等待其他子线程的结束才结束

# 主进程在执行完自己的代码之后不会立即结束 而是等待子进程结束之后 回收子进程的资源
# import time
# from multiprocessing import Process
# def func():
#     time.sleep(5)
#
# if __name__ == '__main__':
#         Process(target=func).start()













