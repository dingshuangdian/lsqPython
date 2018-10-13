"""
一、文件操作
    社会主义价值观.txt
    1、文件路径:d:\社会主义价值观.txt
    2、编码方式:utf-8 gbk ...
    3、操作方式:只读 只写 追加 读写 写读
"""
# 文件读取
f = open('社会主义价值观.txt', mode='r', encoding='utf-8')
content = f.read()
print(content)
f.close()
