import socket
import json
from conf import setting


class MySocketClient:
    def __init__(self):
        self.socket = socket.socket()
        self.socket.connect(setting.addr)

    def mysend(self, msg):
        ret_json = json.dumps(msg)
        self.socket.send(ret_json.encode(setting.code))
