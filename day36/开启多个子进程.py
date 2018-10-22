# Create by dingshuangdian

from multiprocessing import Process
import os


def func(filename, content):
    with open(filename, 'w')as f:
        f.write(content * 10 * '*')


if __name__ == '__main__':
    p_lst = []
    for i in range(10):
        p = Process(target=func, args=('info%s' % i, i))
        p_lst.append(p)
        p.start()

    # for p in p_lst:
    #     p.join()

    [p.join() for p in p_lst]  # 之前所有的进程必须在这里都执行完才能执行下面的代码
    print([i for i in os.walk(r'E:\2018 oldboy Python\Python全栈（第二部分）：并发编程+数据库+前端\1. 并发编程\Day36\day37')])

# 同步 0.1*500=50
# 异步 500 0.1 =0.1
# 多进程写文件
# 首先往文件夹中写文件
# 向用户展示写入文件之后文件夹中所有的文件名
