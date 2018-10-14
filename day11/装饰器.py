# Create by dingshuangdian
# 装饰器形成的过程:最简单的装饰器 有返回值的 有一个参数 万能参数
# 装饰器的作用
# 原则：开放封闭原则
# 装饰器的固定模式

import time


# print(time.time())  # 获取当前时间
# time.sleep(10)  # 让程序在执行到这个位置的时候停一会儿

# def timer(f):  # 装饰器函数
#     def inner():
#         start = time.time()
#         ret = f()  # 被装饰的函数
#         end = time.time()
#         print(end - start)
#         return ret
#
#     return inner
#
#
# @timer  # 语法糖 @装饰器函数名
# def func():  # 被装饰的函数
#     time.sleep(0.01)
#     print("lsqIlvy")
#     return '新年好'
#
#
# # func = timer(func)
#
# ret = func()  # 本质执行inner()
# print(ret)


# 装饰带参数函数的装饰器
# def timer(f):  # 装饰器函数 *args 列表，元组打散
#     def inner(*args, **kwargs):
#         start = time.time()
#         ret = f(*args, **kwargs)  # 被装饰的函数
#         end = time.time()
#         print(end - start)
#         return ret
#
#     return inner
#
#
# @timer  # 语法糖 @装饰器函数名
# def func(a, b):  # 被装饰的函数
#     time.sleep(0.01)
#     print("lsqIlvy", a, b)
#     return '新年好'
#
#
# # func = timer(func)
#
# ret = func()  # 本质执行inner()
# print(ret)


# 装饰器

def wrapper(func):
    def inner(*args, **kwargs):
        r = func(*args, **kwargs)  # 被装饰的函数

        return r

    return inner


@wrapper  # useWrapper=wrapper(useWrapper)
def useWrapper():
    print('useWrapper')
    return '返回值'


useWrapper()
