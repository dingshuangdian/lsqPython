"""
一、文件操作
    社会主义价值观.txt
    1、文件路径:d:\社会主义价值观.txt
    2、编码方式:utf-8 gbk ...
    3、操作方式:只读 只写 追加 读写 写读
    以什么编码方式储存的文件，就以什么编码打开进行操作。



     只读:r  rb存储图片，上传下载等
"""
# 文件读取
f = open('社会主义价值观.txt', mode='r', encoding='utf-8')
content = f.read()
print(content)
f.close()

# 只写 w 不存在的文件则创建，存在，先将源文件的内容全部删除再写入
f = open('只写测试', mode='w', encoding='utf-8')
f.write('只写测试')
f.close()

# wb
# f = open('wb测试', mode='wb')
# f.write('wb测试'.encode('utf-8'))  # byte转换成字符串
# f.close()

# 追加 a ab
#
# f = open('wb测试', mode='a', encoding='utf-8')
# f.write('追加测试')
# f.close()

# f = open('wb测试', mode='ab')
# f.write('ab追加测试'.encode('utf-8'))
# f.close()


# 读写 r+ r+b
f = open('wb测试', mode='r+', encoding='utf-8')
print(f.read())
f.write('lsq,ily')
print(f.read())
f.close()

# f = open('wb测试', mode='r+b')
# print(f.read())
# f.write('lsq,ily'.encode('utf-8'))
# print(f.read())
# f.close()
# 最常用r+ w

# w+ 写读

# f = open('wb测试', mode='w+', encoding='utf-8')
# f.write('lsq,ily')
# f.seek(0)  # 调节光标
# print(f.read())
# f.close()

# 功能详解
# f = open('社会主义价值观.txt', mode='r+', encoding='utf-8')
# # content = f.read(3)  # read读出来的都是字符
# count = f.tell()  # 查询当前光标位置
# f.seek(count - 9)  # 光标是按字节定光标位置(utf8 3个字节表示一个中文字符)  移动光标位置+ -
# f.readable()  # 是否可读
# f.readline()  # 读行(一行一行读)
# f.readlines()  # 每一行当成列表中的一个元素添加到列表List中
# content = f.read()
# print(content)
# f.close()

# 另一种读写文件的方式(同时打开多个文件)
with open('社会主义价值观.txt', mode='r+', encoding='utf-8') as f, \
        open('wb测试', mode='w+', encoding='utf-8')as f1:
    print(f.read())
    print(f1.read())
