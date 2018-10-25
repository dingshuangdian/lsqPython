import os
import sys
import socketserver
from core.server import MyFTPServer

sys.path.append(os.path.dirname(os.getcwd()))

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8990), MyFTPServer)
    server.serve_forever()
