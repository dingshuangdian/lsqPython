import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 8080))
while 1:
    msg = input('>>>')
    if msg == 'bye':
        sk.send(b'hi')
        break
    sk.send(b'client2:' + msg.encode('utf-8'))

    ret = sk.recv(1024).decode('utf-8')
    if ret == 'bye': break
    print(ret)
sk.close()
