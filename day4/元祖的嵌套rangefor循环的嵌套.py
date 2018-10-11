# 元祖的嵌套range for循环的嵌套
# 列表的嵌套

li = ['lsq', 'dsd', 'bsg', 'nmc']
print(li[1][1])
name = li[0].capitalize()  # 首字母大写
print(name)
li[2] = li[2].replace('bs', 'sd')
print(li[2])

# 元祖 只读列表，可循环查询，可切片。
# 儿子不能改，孙子可能可以改

# ps 更改属于列表的属性可改，属于元祖则不可改
tu = (1, 2, 3, 'abc', [2, 3, 4, 'dsd'], 'easton')
print(tu[3])
print(tu[0:4])
for i in tu:
    print(i)
tu[4][3] = tu[4][3].upper()
print(tu)
tu[4].append('lsq')
print(tu)
# join (iterable:可迭代对象)
s = 'lsq'
s1 = '_'.join(s)
print(s1)

l = ['123', 'abc', 'dsd', 'easton']
print(''.join(l))
