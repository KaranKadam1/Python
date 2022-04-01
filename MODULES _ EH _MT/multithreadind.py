# multiprograming = having more than 2 program/process in memory for execution
# thread = sequence of instructions which cpu going to run is called thread
# thread is a sequence of intrsuctions which act as an execution path for cpu
# one thread in aplication is common is called single thread
# an aplication has multiple execution path is called multithreaded application(all apk now are mt)

# use idle for multithreading
# single threaded-->
import time
def display():
    data = "Firstbit Solution"
    for ch in data:
        print(ch,end=" ")
        time.sleep(1)
display()
display()


# multithreading-->
import time
import threading
def display():
    data = "Firstbit Solution"
    for ch in data:
        print(ch,end=" ")
        time.sleep(1)
t1 = threading.Thread(name="Thread1",target=display)
# we are creating thread thread 1 which is going execute method display
t1.start()
# to execute the thread
display()#this method will be called by default thread present in application 



import time
import threading
def display(data):
    for ch in data:
        print(ch,end=" ")
        time.sleep(1)
t1 = threading.Thread(name="Thread1",target=display,args=("Firstbit solution",))
t1.start()
display("Microsoft corp")




from threading import Thread
class myThread(Thread):
    def __init__(self,data):
        super().__init__()
        self.data = data
    def display(self):  
        for ch in self.data:
            print(ch,end=" ")
            time.sleep(1)
    def run(self):
        # the task we want to perform using thread should be within run method
        self.display()
# t1 = myThread("Firstbit Solution")
# t2 = myThread("secondbit solution")
# t1.start()
# t2.start()

# for more req like t1 and t3 first start then remaining
t1 = myThread("111111111")
t2 = myThread("222222222")
t3 = myThread("444444444")
t4 = myThread("555555555")
t1.start()
t1.join(4) #after t1 4 sec all threads runs in parallel
t2.start()
t3.start()
t4.start()


#Race Condition= final ans depends on which thread performs last write 
#criticle section problem= a set of instruction which access the shared data.this is called criticle problem.
# eg.vinayak vaishali taking class on same time -->to avoid we can lock our resource and after work done we can release
import threading

def increament_4():
    global x
    for i in range(100000):
        # criticle section
        lock.acquire()  #without lock it will gives randoms + - values
        x = x+4
        lock.release()

def increament_1():
    global x
    for i in range(100000):
        lock.acquire()
        x = x+1
        lock.release()

def decreament_3():
    global x
    for i in range(100000):
        lock.acquire()
        x = x-3
        lock.release()

def decreament_2():
    global x
    for i in range(100000): 
        lock.acquire()
        x = x-2
        lock.release()
    
if __name__ == '__main__':
    global x
    lock = threading.Lock()
    x = 0
    print("initial value of x= ",x)
    t1 = threading.Thread(name="Thread1",target=increament_1)
    t2 = threading.Thread(name="Thread2",target=increament_4)
    t3 = threading.Thread(name="Thread3",target=decreament_2)
    t4 = threading.Thread(name="Thread4",target=decreament_3)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    print("final value of x=",x)