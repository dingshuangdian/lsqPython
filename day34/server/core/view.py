from core.user import User
import os
import pickle
from conf import setting


def login(msg):
    print(msg)


def register(msg):
    # username,password
    # 创建一个属于这个用户的家目录
    # 把用户名密码 写进userinfo文件里，记录用户名
    # 记录用户的初始磁盘配额
    # 记录文件大小
    # 记录用户当前所在的目录
    # print(msg)
    user_obj = User(msg['username'])  # 记录用户的信息在内存里
    pickle_path = os.path.join(setting.pickle_path, msg['username'])

    with open(pickle_path, 'wb') as f:
        pickle.dump(user_obj, f)

    os.mkdir(user_obj.home)  # 创建一个属于这个用户的家目录
    with open(setting.user_info, 'a')as f:
        f.write('%s|%s|%s\n' % (msg['username'], msg['password'], pickle_path))

    return True, pickle_path


def upload(msg):
    print(msg)


def download(msg):
    print(msg)
