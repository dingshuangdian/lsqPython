# property

# 内置装饰器函数 只在面向对象中使用  伪装成属性

from math import pi


class Circle:
    def __init__(self, r):
        self.r = r

    @property  # 把方法伪装成属性
    def perimeter(self):
        return 2 * pi * self.r

    @property
    def area(self):
        return self.r ** 2 * pi


cl = Circle(5)
# print(cl.area())
# print(cl.perimeter())
print(cl.area)
print(cl.perimeter)
# class Person:
#     def __init__(self,name,high,weight):
#         self.name = name
#         self.high = high
#         self.weight = weight
#     @property
#     def bmi(self):
#         return self.weight / self.high**2

# jin = Person('金老板',1.6,90)
# jin.bmi = 18
# classmethod
# staticmethod

# class Person:
#     def __init__(self,name):
#         self.__name = name
#     @property
#     def name(self):
#         return self.__name + 'sb'
#     @name.setter
#     def name(self,new_name):
#         self.__name = new_name
#
# tiger = Person('泰哥')
# print(tiger.name)
# tiger.name = '全班'
# print(tiger.name)

# class Goods:
#     discount = 0.8
#     def __init__(self,name,price):
#         self.name = name
#         self.__price = price
#     @property
#     def price(self):
#         return self.__price * Goods.discount
# apple = Goods('苹果',5)
# print(apple.price)

# 属性 查看 修改 删除
# class Person:
#     def __init__(self,name):
#         self.__name = name
#         self.price = 20
#     @property
#     def name(self):
#         return self.__name
#     @name.deleter
#     def name(self):
#         del self.__name
#     @name.setter
#     def name(self,new_name):
#         self.__name = new_name
# brother2 = Person('二哥')
# del Person.price
# brother2.name = 'newName'
# brother2
# del brother2.name
# print(brother2.name)
