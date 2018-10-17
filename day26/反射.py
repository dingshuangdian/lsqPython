class A: pass


class B(A): pass


a = A()
# print(isinstance(a, A))  # 判断对象是否属于类的对象

# print(issubclass(B, A))  # 判断子类和父类的关系

# 反射  (非常重要)用字符串类型的名字去操作变量

name = 1


# eval('print(name)')  # 安全隐患

# 反射 就没有安全问题 是用字符串类型的名字 去操作 变量
# 反射对象中的属性和方法  #hasattr getattr setattr delattr
class A:
    def func(self):
        print('in func')


a = A()
a.name = 'lsq'
a.age = 21

# 反射对象的属性

ret = getattr(a, 'name')  # 通过变量名的字符串形式取到的值
print(ret)

变量名 = input('>>>>>')


# print(getattr(a, 变量名))

# print(a.__dict__[变量名])

# 反射对象的方法
# ret = getattr(a, 'func')  # 得到方法的内存地址
# ret()

class A:
    price = 20

    @classmethod
    def func(cls):
        print('in func cls')


# 反射类的属性
# A.price
print(getattr(A, 'price'))

# 反射类的方法:classmethod staticmethod

# A.func()
# if hasattr(A, 'func'):
#     getattr(A, 'func')()

import mymodul

# 反射模块的属性

# print(mymodel.day)
print(getattr(mymodul, 'day'))
# 反射模块的方法
getattr(mymodul, 'getA')()

# 反射自己模块中的变量 方法
import sys


def qqxing():
    print('qqxing')


year = 2018


# print(getattr(sys.modules['__main__'], 'year'))
# getattr(sys.modules['__main__'], 'qqxing')()
# print(getattr(sys.modules[__name__], 变量名))
# getattr(sys.modules[__name__], 变量名)()
# 要反射的函数有参数怎么办?
# print(time.strftime('%Y-%m-%d %H:%M:S'))
# print(getattr(time,'strftime')('%Y-%m-%d %H:%M:S'))

# 一个模块中的类能不能反射得到
# import my
# print(getattr(my,'C')())
# if hasattr(my,'name'):
#     getattr(my,'name')

# 重要程度半颗星
# setattr  设置修改变量
class A:
    pass


a = A()
setattr(a, 'name', 'nezha')
setattr(A, 'name', 'alex')
print(A.name)
print(a.name)

# delattr 删除一个变量
delattr(a, 'name')
print(a.name)
delattr(A, 'name')
print(a.name)
