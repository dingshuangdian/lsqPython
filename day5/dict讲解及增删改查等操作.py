# dict
"""
数据类型划分:可变数据类型，不可变数据类型
不可变数据类型:元祖，bool, int str 可哈希
可变数据类型：list  dict set  不可哈希

dict key 必须是不可变数据类型,可哈希《
    value:任意数据类型.
    dict 优点:二分查找去查
        存储大量的关系型数据
        特点;无序的
"""
dic1 = {'age': 18, 'name': 'kim', 'job': 'code'}
dic = {
    'name': ['lsq', 'dsd', 'bsg', 'nmc'],
    'py9': [{'num': 71, 'avg_age': 18}],
    True: 1,
    (1, 2, 3): 'lsq',
    2: '三哥'

}

# 增
dic1['hight'] = 175  # 如果没键值对，添加
dic1['age'] = 16  # 如果有键值对，则值覆盖

dic1.setdefault('weight', 150)  # setdefault 设置默认，有键值对则不变，没有则添加
dic1.setdefault('name', '四哥')
print(dic1)

# 删
# print(dic1.pop('age'))  # 有返回值
# print(dic1.pop('二哥', "键不存在"))  # 不确定是否存在键+none
# print(dic1)
#
# print(dic1.popitem())  # 随机删除 有返回值 元祖里面是删除的键值
#
# del dic1['name']
#
# del dic1
# dic1.clear()  # 清空字典


# 改 updata

# dic1['age']=16
dic2 = {'age': 18, 'name': 'kim'}
dic3 = {'job': 'code', 'name': 'lsq'}
dic3.update(dic2)  # dic2的键值对添加到dic3有的覆盖，没的添加
print(dic2)
print(dic3)

# 查
dic5 = {'age': 18, 'name': 'kim', 'job': 'code'}

print(dic5.keys(), type(dic5.keys()))
print(dic5.values())
print(dic5.items())
for i in dic5:  # 默认打印键
    print(i)

for i in dic5.values():
    print(i)
for k, v in dic5.items():
    print(k, v)
# demo 一行代码互换ab值
a = 1
b = 2
a, b = b, a
print(dic5['age'])
print(dic5.get('age', "没有这个键"))  # 容错
