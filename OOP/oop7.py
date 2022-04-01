# class Time:
    
#     def getData(self):
#         self.hr = int(input("enter hr="))
#         self.mm = int(input("enter mm="))
#         self.ss = int(input("enter ss="))
    
#     def showData(self):
#         print("{0}:{1}:{2}".format(self.hr,self.mm,self.ss))

# t1 = Time()
# t1.getData()
# t1.showData()

# hr,mm,ss depend of object
# hr,mm,ss are instance variable(it belongs to object)
# no of copies of instance varible depends on no.of object i.e 3hr->3objects

# instance means seperate copies
# static = belongs to all object (1 copy share by all objects) belongs to class
# non-static=belongs to object.(called using object)(object level)

class Time:
    # static  variable
    count = 0

    def __init__(self,hr=10,min=10,sec=10):
        self.hr = hr   #self.hr=iv
        self.mm = min
        self.ss = sec
        Time.count += 1 #static variables are refered using class name./without class it just a normal local variable
        
    def showTime(self):
        print("{0}:{1}:{2}".format(self.hr,self.mm,self.ss))
        
    # this method should called by class not by object
    def showcount():
        print("num of objects{0}".format(Time.count))
        
Time.showcount()

t1=Time()
t1.showTime()
t2 = Time(1,2,3)
t2.showTime()

Time.showcount()

