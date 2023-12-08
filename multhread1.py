# without creating class

# from threading import *
# def hello():
#     print("HELLO")
# t1=Thread(target=hello)
# t1.start()    



# without extending thread class

# from threading import *
# class A:
#     def hello(self):
#         print("HELLO")
# a=A()
# t1=Thread(target=a.hello)
# t1.start()        


# thread synchronization

from threading import *
from time import sleep
counter=0
def increment(x,y):
    global counter
    y.acquire()
    local_counter=counter
    local_counter+=x
    sleep(0.2)
    counter=local_counter
    print("inside:",counter)
    y.release()
l=Lock()    
t1=Thread(target=increment,args=(5,l))
t2=Thread(target=increment,args=(10,l))
t1.start()
t2.start()
t1.join()
t2.join()
print("outside:",counter)





