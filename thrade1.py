#import threading
#print("Current thread is:",threading.current_thread().getName())
from threading import *
class MyThread(Thread):
    def run(self):
        for i in range(10):
            print("child thread-1")
t=MyThread()
t.start()
for i in range(10):
    print("main thread-1")
'''def display():
    
    for i in range(1,11):
        print(i)
t=Thread(target=display) #thread object
t.start()
for i in range(1,11):
    print("main thread")'''
