# Create by dingshuangdian

import socket
import subprocess
while 1:
    sk = socket.socket()
    sk.connect(('127.0.0.1', 8090))
    cmd = sk.recv(1024).decode('gbk')
    ret = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    std_out = 'stdout:' + (ret.stdout.read()).decode('gbk')
    std_err = 'stdeer:' + (ret.stderr.read()).decode('gbk')
    print(std_out)
    print(std_err)
    sk.send(std_out.encode('utf-8'))
    sk.send(std_err.encode('utf-8'))
    sk.close()
