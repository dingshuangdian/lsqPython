# 数据类型整体分析

# 数据类型
"""
int 1,2,3用于计算
bool：True，False,用于判断
str: "abc","lsq"

list:[]
元祖:只读(1,2,3,'无权限')
dict:字典(键值对){'name':'lsq','age':18}
集合:{1,2,3,4,5}(少用)
"""
# int

i = 2
print(i.bit_length())  # 数值转换成2进制最小的位数

# bool True False

# int---->bool 只要是0-------》False 非0就是True
i1 = 3
b = bool(i1)
print(b)

'''
ps:
while True:
    pass
while 1:  (效率高)
    pass
'''

# str -->bool 空或者null为False 非空为True

# demo
s = ''
if s:
    print("")
else:
    print("您输入的内容为空")

'''
str索引切片
'''
s1 = 'ADFJKSFKSHGSKGHSKG'
print(s1[0])
# 切片(顾头不顾尾)
s2 = s1[0:3]
print(s2)  # ADF
s3 = s1[-1]  # 取字符串最后一位
print(s3)
s4 = s1[:]  # 全部取出
print(s4)
s5 = s1[0:5:2]  # s1[首:尾:步长]
print(s5)
s6 = s1[5:0:-2]  # 反取
print(s6)
