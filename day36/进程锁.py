# 锁
# 火车票
import json
import time
from multiprocessing import Process
from multiprocessing import Lock


#
# def show():
#     with open('ticket') as f:
#         dic = json.load(f)
#
#     print('余票:%s' % dic['ticket'])


def buy_ticket(i, lock):
    lock.acquire()  # 拿钥匙开门
    with open('ticket') as f:
        dic = json.load(f)
        time.sleep(0.1)

    if dic['ticket'] > 0:
        dic['ticket'] -= 1
        print('\033[32m%s买到票了\033[0m' % i)

    else:
        print('\033[31m%s没买到票\033[0m' % i)
    time.sleep(0.1)

    with open('ticket', 'w') as f:
        json.dump(dic, f)

    lock.release()  # 还钥匙


if __name__ == '__main__':
    # for i in range(10):
    #     p = Process(target=buy_ticket, args=(i))
    #     p.start()
    lock = Lock()
    # Lock.acquire()
    for i in range(10):
        p = Process(target=buy_ticket, args=(i, lock))
        p.start()
