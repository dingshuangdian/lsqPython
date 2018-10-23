# struct模块
# 什么是固定长度的Bytes
# 为什么要转成固定长度的bytes
import struct

ret = struct.pack('i', 4096)  # i 代表int 就是即将要把一个数字转换成固定长度的bytes类型
print(ret)
num = struct.unpack('i', ret)
print(num)
print(num[0])
