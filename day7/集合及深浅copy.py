# 集合及深浅copy
'''
集合：可变的数据类型，它里面的元素必须是不可变的数据类型，无序，不重复
{}
'''
# 集合创建
set1 = set({1, 2, 3})
# set2 = {1, 2, 3, [2, 3], {'name': 'lsq'}}#错的
set3 = {'lsq', 'dsd', 'bsg', 'nmc', 'nmc'}
print(set3, type(set3))
# add
# set3.add('女神')
# updata
# set3.update('abc')
# 删除
# set3.pop()  # 随机删除
# print(set3.pop())  # 返回值
#
# set3.remove('nmc')#按元素删除
# set3.clear()
# del set3

# 查
# for i in set3:
#     print(i)


# 交集
# set1 = {1,2,3,4,5}
# set2 = {4,5,6,7,8}
# set3 = set1 & set2
# print(set3)  # {4, 5}
# print(set1.intersection(set2))  # {4, 5}

# 并集
# set1 = {1,2,3,4,5}
# set2 = {4,5,6,7,8}
# print(set1 | set2)  # {1, 2, 3, 4, 5, 6, 7,8}
# print(set2.union(set1))  # {1, 2, 3, 4, 5, 6, 7}

# set1 = {1,2,3,4,5}
# set2 = {4,5,6,7,8}
# print(set1 ^ set2)  # {1, 2, 3, 6, 7, 8}
# print(set1.symmetric_difference(set2))  # {1, 2, 3, 6, 7, 8}

# set1 = {1,2,3,4,5}
# set2 = {4,5,6,7,8}
# print(set1 - set2)  # {1, 2, 3}
# #set1独有的
# print(set1.difference(set2))  # {1, 2, 3}

# set1 = {1,2,3,}
# set2 = {1,2,3,4,5,6}
#
# print(set1 < set2)
# print(set1.issubset(set2))  # 这两个相同，都是说明set1是set2子集。

# print(set2 > set1)
# print(set2.issuperset(set1))  # 这两个相同，都是说明set2是set1超集。


# 去重
li = [1, 2, 33, 33, 2, 1, 4, 5, 6, 6]
set1 = set(li)
# print(set1)
li = list(set1)
print(li)
s1 = {1, 2, 3}
print(s1, type(s1))
# 转换成不可变的数据类型
# s = frozenset('barry')
# print(s,type(s))
# for i in s:
#     print(i)
