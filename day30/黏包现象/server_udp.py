# Create by dingshuangdian
import socket

while 1:
    sk = socket.socket(type=socket.SOCK_DGRAM)
    sk.bind(('127.0.0.1', 8090))
    msg, addr = sk.recvfrom(1024)
    cmd = input('>>>>>>')
    sk.sendto(cmd.encode('utf-8'), addr)
    msg, addr = sk.recvfrom(1024)
    print(msg.decode('utf-8'))
sk.close()

# udp不会黏包，但是udp会丢包
