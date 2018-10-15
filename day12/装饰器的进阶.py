# Create by dingshuangdian

from functools import wraps


def wrapper(func):  # func = holiday
    @wraps(func)
    def inner(*args, **kwargs):
        print('在被装饰的函数执行之前做的事')
        ret = func(*args, **kwargs)
        print('在被装饰的函数执行之后做的事')
        return ret

    return inner


@wrapper  # holiday = wrapper(holiday)
def holiday(day):
    '''这是一个放假通知'''
    print('全体放假%s天' % day)
    return '好开心'


# 要获取holiday属性导入装饰器:wraps装饰inner
print(holiday.__name__)
print(holiday.__doc__)
ret = holiday(3)  # inner
print(ret)

# def wahaha():
#     '''
#     一个打印娃哈哈的函数
#     :return:
#     '''
#     print('娃哈哈')

# print(wahaha.__name__) #查看字符串格式的函数名
# print(wahaha.__doc__)  #document


# 带参数的装饰器
import time

FLAG = True


def timer_out(flag):
    def timmer(func):
        def inner(*args, **kwargs):
            if flag:
                start = time.time()
                ret = func(*args, **kwargs)
                end = time.time()
                print(end - start)
                return ret

            else:
                ret = func(*args, **kwargs)
                return ret

        return inner

    return timmer


@timer_out(FLAG)
def wahahah():
    time.sleep(0.1)
    print('wawawawawa')


@timer_out(FLAG)
def erguotou():
    time.sleep(0.1)
    print('111111111111')


# wahahah()
# erguotou()

# 多个装饰器装饰一个函数
def wrapper1(func):
    def inner1():
        print('wrapper1,before func')
        ret = func()
        print('wrapper1,after func')
        return ret

    return inner1


def wrapper2(func):
    def inner2():
        print('wrapper2,before func')
        ret = func()
        print('wrapper2,after func')
        return ret

    return inner2


def wrapper3(func):
    def inner3():
        print('wrapper3,before func')
        ret = func()
        print('wrapper3,after func')
        return ret

    return inner3


@wrapper1  # f=wrapper2(f)-->wrapper2(inner1)==inner2
@wrapper2  # f=wrapper1(f)=inner1
@wrapper3
def f():
    print('int f')
    return '1223'


print(f())
# 执行过程按照@顺序执行被装饰函数之前的代码，再按照@逆时针执行被装饰函数之后的代码
