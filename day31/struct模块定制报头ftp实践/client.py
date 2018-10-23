# 发送端
import socket
import os
import json
import struct

sk = socket.socket()
sk.connect(('127.0.0.1', 8090))
# 发送文件
buffer = 1024
filepath = r'C:\Users\easton\video\Python全栈（第一部分）：基础+模块+面向对象+网络编程\day32'
head = {'filepath': filepath,
        'filename': r'01 python fullstack s9day32 复习.mp4',
        'filesize': None

        }

filesize = os.path.getsize(os.path.join(head['filepath'], head['filename']))
head['filesize'] = filesize
json_head = json.dumps(head)  # 字典转成了字符串
bytes_head = json_head.encode('utf-8')
# 计算head的长度
head_len = len(bytes_head)  # 报头的长度
pack_len = struct.pack('i', head_len)
sk.send(pack_len)  # 先发报头的长度
sk.send(bytes_head)  # 再发送bytes类型的报头
with open(filepath, 'rb') as f:
    while filesize:
        print(filesize)
        if filesize >= buffer:
            content = f.read(buffer)  # 每次读出来的内容
            sk.send(content)
            filesize -= buffer
        else:
            content = f.read(filesize)
            sk.send(content)
            break

sk.close()
