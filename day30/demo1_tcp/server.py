import socket

sk = socket.socket()  # 创建一个socket对象
sk.bind(('127.0.0.1', 8080))  # 给server绑定一个ip和端口
sk.listen()
while 1:
    conn, addr = sk.accept()  # 获取到一个客户端的连接，已经完成了三次握手建立了一个连接
    while 1:
        msg = conn.recv(1024).decode('utf-8')  # 阻塞，直接收到一个客户端发来的消息
        print(msg)
        if msg == 'bye': break
        info = input('>>>')
        if info == 'bye':
            conn.send(b'bye')
            break
        conn.send(info.encode('utf-8'))  # 发消息
    conn.close()  # 关闭连接
sk.close()  # 关闭socket对象，如果不关闭，还能继续接收
