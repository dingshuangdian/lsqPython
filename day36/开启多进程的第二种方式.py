# Create by dingshuangdian
from multiprocessing import Process
import os


class MyProcess(Process):
    def __init__(self, arg1, arg2):
        super().__init__()  # 调用父类的init方法
        self.arg1 = arg1
        self.arg2 = arg2

    def run(self):
        print(os.getpid())
        print(self.arg1)
        print(self.arg2)


if __name__ == '__main__':
    print('主:', os.getpid())
    p1 = MyProcess(1, 2)
    p1.start()

# 自定义类 继承Process类
# 必须实现一个run方法 run方法中是在子进程中执行的代码
