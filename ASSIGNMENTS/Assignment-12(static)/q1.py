'''
1. Create a class Book with members as bid,bname,price and 
author.Add following methods: 
a. Constructor (Support both parameterized and parameterless) 
b. Destructor 
c. ShowBook 
d. Add static variable count and also maintain count of objects 
created

'''
class Book:
    
    count = 0
    def __init__(self,b=101,n="python",p=200,a="abc"):  #Parameterized Constructor
        Book.count += 1

        self.bid = b
        self.bname = n
        self.price = p
        self.author = a
    
    def ShowBook(self):
        print("Bid = {0}".format(self.bid))
        print("Bname = {0}".format(self.bname))
        print("Price = {0}".format(self.price))
        print("Author = {0}\n".format(self.author))

    def Showcout():
        print("no. of objects created are {0}".format(Book.count))
    
    def __del__(self):  #Destructor
        print("Object Destroyed")

b1 = Book()
b1.ShowBook()
b2 = Book(102,"cpp",300,"kkk")
b1.ShowBook()
Book.Showcout()


