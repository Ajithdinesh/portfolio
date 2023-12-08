from threading import *
from time import sleep
class A(Thread):
    def run (self):
        for i in range(5):
            print("HELLO",current_thread().name)
            sleep(1)
class B(Thread):
    def run(self):
        for i in range(5):
            print("HIII",current_thread().name)
            sleep(1)
obj1=A()
obj1.start()
sleep(0.2)
obj2=B()
obj2.start()    
obj1.join()
obj2.join()
print("BYE",current_thread().name)

# by extending thread class
