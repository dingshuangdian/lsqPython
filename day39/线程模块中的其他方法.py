import time
import threading


def wahaha(n):
    time.sleep(0.5)
    print(n, threading.current_thread(), threading.get_ident())


for i in range(10):
    threading.Thread(target=wahaha, args=(i,)).start()
print(threading.active_count())  # 10
print(threading.current_thread())
print(threading.enumerate())
