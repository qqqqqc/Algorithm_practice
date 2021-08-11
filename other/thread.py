# 两个线程舒徐打印 12A 34B 56C 78D
import threading,time

def thread1():
    for i in range(1,53,2):
        t2_lock.acquire()
        print(i,end="")
        print(i+1,end="")
        t1_lock.release()


def thread2():
    for i in range(26):
        t1_lock.acquire()
        print(chr(ord("A")+i))
        t2_lock.release()


t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)

t1_lock = threading.Lock()
t2_lock = threading.Lock()

t1_lock.acquire()

t1.start()
t2.start()