# Create by dingshuangdian

# 只要含有yield关键字的函数都是生成器函数，只能存在函数体里，不能跟return共用
def generator():
    print(1)
    yield 'a'
    print(2)
    yield 'b'


# 生成器函数：执行之后会得到一个生成器作为返回值
# yield与return区别：return后的代码都不会执行。 yield不会停止执行
ret = generator()
# print(ret)
# # 也是一个迭代器
# ret1 = ret.__next__()
# # ret.__iter__()
# print(ret1)
# ret2 = ret.__next__()
# # ret.__iter__()
# print(ret2)

for i in ret:
    print(i)


# 哇哈哈
def wahaha():
    for i in range(20):
        yield '哇哈哈%s' % i


g = wahaha()

for i in g:
    print(i)
