# 实现一个大文件的上传或者下载

import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 8090))

