'''
python2 python3
'''
# python2
# print() print 'abc'  #可加括号可不加
# range() xrange()  生成器
# raw_input()

# python3
# print('abc')#必须加括号
# range()
# input()


# = == is
# = 赋值 ==比较值是否相等 is:比较，比较的是内存地址 id:(内容)
# li1 = [1, 2, 3]
# li2 = li1
# print(id(li1), id(li2))
# print(li1 is li2)

# 数字，字符串 小数据池
# 数字的范围 -5--256
# 字符串：1，不能有特殊字符 2，s*20还是同一个地址，s*21以后都是两个地址
# 剩下的list dict tuple set 没有小数据池概念


"""
编码


ascii   A:00000010   8位 一个字节


unicode  A:00000000 00000000 00000010 00000001 32位 四个字节
            中:00000000 00000000 00000010 00000001 32位 四个字节


utf-8  A:0010 0000 8位 一个字节
        中:00000000 00000000 00000010  24位 三个字节


gbk     A: 00000110 8位  一个字节
        中:00000000 00000000  16位 两个字节
        
        
1、各个编码之间的二进制，是不能相互识别的，会产生乱码
2、文件的储存传输，不能是unicode（只能是utf-8 utf-16 gbk gb2312 ascii 等）

"""

'''
py3：
    str 在内存中是用unicode编码。
    bytes类型 
    
    对于英文:
        str ：表现形式:  s='lsq'
             编码方式 01010101 unicode
        bytes: 表现形式： s=b'lsq'
                编码方式: 0001000100 utf-8 gbk ....
                
                
    对于中文：
        str ：表现形式:  s='中国'
            编码方式 01010101 unicode
        bytes: 表现形式： s=b'x\e91\e91\e91\e01\e21'
            编码方式: 0001000100 utf-8 gbk  ....

'''
# demo
s1 = 'lsq'
# encode 编码，如何将str--->bytes
sll = s1.encode('utf-8')
print(sll)

s2 = '中国'
s22 = s2.encode('utf-8')
print(s22)
s22 = s2.encode('gbk')
print(s22)
