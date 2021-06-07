from threading import Thread
from threading import current_thread
from queue import Queue
import random

q = Queue(5)


class ProducerThread(Thread):
    def run(self):
        t_name = current_thread().getName()
        pdcs = range(100)
        global q
        while True:
            pdc = random.choice(pdcs)
            q.put(pdc)
            print('%s create %s' %(t_name, pdc))


class ConsumerThread(Thread):
    def run(self):
        t_name = current_thread().getName()
        global q
        while True:
            pdc = q.get()
            print('%s consume %s' % (t_name, pdc))


pt1 = ProducerThread()
pt2 = ProducerThread()
pt1.start()
pt2.start()

ct1 = ConsumerThread()
ct1.start()

