import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1', 8080))

while 1:
    msg, addr = sk.recvfrom(1024)
    print(msg.decode('utf-8'))
    info = input('>>>').encode('utf-8')
    sk.sendto(msg, addr)

sk.close()
