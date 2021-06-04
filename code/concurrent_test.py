import threading
from threading import current_thread


class MyThread(threading.Thread):
    def run(self):
        print(current_thread().getName(), 'start')
        print('run')
        print(current_thread().getName(), 'stop')


t1 = MyThread()
t1.start()
t1.join()  # 主线程等待执行结束
print(current_thread().getName(), 'stop')

