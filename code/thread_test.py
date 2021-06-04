import threading
import time
from threading import current_thread


def myThread(a1, a2):
    print(current_thread().getName(), 'start')
    print('%s %s' % (a1, a2))
    time.sleep(1)
    print(current_thread().getName(), 'end')


for i in range(1, 6, 1):
    t1 = threading.Thread(target=myThread, args=(i, i + 1))
    t1.start()


print(current_thread().getName(), 'end')
