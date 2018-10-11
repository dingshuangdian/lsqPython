# 列表的增删改查以及嵌套

li = ['lsq', 'dsd', 'easton']
l1 = li[0]
print(l1)
l2 = li[1]
print(l2)
l3 = li[0:3]
print(l3)

# 增加 append insert
li.append('zxx')
li.append('xnl')
print(li)

# while 1:
#     username = input('>>>')
#     if username.split().upper() == 'Q':
#         break
#     else:
#         li.append(username)
# print(li)

li.insert(1, 'lsqdsd')
# print(li)
li.extend('中国')
# print(li)

# 删
# name = li.pop(1)  # 返回值
# name = li.pop()  # 默认删除最后一个
# li.remove('lsq')  # 按元素去删除
# li.clear()  # 清空

# del li
# del li[0:2]  # 切片去删除

# 改
# li[0] = '女神'
# li[0] = [1, 2, 3]
# li[0:2] = 'hghf'  # 切片改(把前两个拿出来，添多少无所谓)
# li[0:2] = [1, 2, 3, '三岔河']

# 查
# for i in li:
#     print(i)
# print(li[0:2])

# 公共方法
# l5 = len(li)
# print(l5)
# num = li.count('lsq')
# print(li.index('lsq'))
# 排序(正序)
lii = [1, 5, 4, 7, 6, 2, 3]
lii.sort()
print(lii)
# 倒叙
lii.sort(reverse=True)
print(lii)
# 反转
lii.reverse()
print(lii)
