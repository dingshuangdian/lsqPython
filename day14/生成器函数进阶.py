# 生成器函数进阶
def gennerator():
    print(123)
    content = yield 1
    print('=========', content)
    print(456)
    yield 2


g = gennerator()  # 返回一个生成器(yield)

ret = g.__next__()
print('***', ret)
# ret = g.__next__()
ret = g.send('hello')  # send的效果和next一样
print('***', ret)


# send获取下一个值的效果和next基本一致
# 只是在获取下一个值的时候，给上一个值的位置传递一个数据

# 使用send的注意事项
# 第一次使用生成器的时候，首先使用Next获取下一个值
# 最后一个yield不能接收外部的值


# 实例  获取移动平均值
# def average():
#     sum = 0
#     count = 0
#     avg = 0
#     while True:
#         num = yield avg
#         sum += num
#         count += 1
#         avg = sum / count
#
#
# avg_g = average()  # 拿到生成器
# avg_g.__next__()
# avg1 = avg_g.send(10)
# avg1 = avg_g.send(20)
# print(avg1)

# 带装饰器
def init(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.__next__()
        return g

    return inner


@init
def average():
    sum = 0
    count = 0
    avg = 0
    while True:
        num = yield avg
        sum += num
        count += 1
        avg = sum / count


avg_g = average()
ret = avg_g.send(10)
print(ret)

# 推荐两本书 《流畅的python》、《 核心编程》
