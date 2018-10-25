import json
import socketserver
from core import view
from conf import setting


class MyFTPServer(socketserver.BaseRequestHandler):
    logined_lst = {}  # 已登录的列表

    def handle(self):
        while True:

            msg = self.my_recv()
            print(MyFTPServer.logined_lst)

            # 消息的转发 把任务转给view文件中对应的方法
            op_str = msg['operation']

            if op_str == 'login' or op_str == 'register':
                if hasattr(view, op_str):
                    func = getattr(view, op_str)
                    ret, pickle_path = func(msg)
                if ret == True:
                    MyFTPServer.logined_lst[self.client_address] = pickle_path  # 用户的pickle信息所在的文件地址
                    self.my_send(ret)

            elif hasattr(view, op_str) and self.client_address in MyFTPServer.logined_lst:
                func = getattr(view, op_str)
                ret = func(msg, self.request)
                self.my_send(ret)

            else:
                self.my_send(False)

            # msg
            # 登录  注册
            # 查看目录
            # 上传文件
            # 反射

    def my_recv(self):  # 派生方法
        msg = self.request.recv(1024)
        msg = json.loads(msg.decode(setting.code))
        return msg

    def my_send(self, msg):
        msg = json.dumps(msg).encode(setting.code)
        self.request.send(msg)
