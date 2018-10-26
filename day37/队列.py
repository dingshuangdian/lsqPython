# 队列 先进先出
# IPC
# from multiprocessing import Queue
# q = Queue(5)
# q.put(1)
# q.put(2)
# q.put(3)
# q.put(4)
# q.put(5)
# print(q.full())   # 队列是否满了
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.empty())
# while True:
#     try:
#         q.get_nowait()
#     except:
#         print('队列已空')
#         time.sleep(0.5)
# for i in range(6):
#     q.put(i)

from multiprocessing import Queue, Process


def produce(q):
    q.put('hello')


def consume(q):
    print(q.get())


if __name__ == '__main__':
    q = Queue()
    p = Process(target=produce, args=(q,))
    p.start()
    c = Process(target=consume, args=(q,))
    c.start()
