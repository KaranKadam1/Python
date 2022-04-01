# Create a class book with members as bid,bname,price and author.
# Add Following method:
# a.Constructor (Support both parameterized and Patameterless)
# b.Destructor
# c.ShowBook

class Book:

    def __init__(self,b,n,p,a):  #Parameterized Constructor
        self.bid = b
        self.bname = n
        self.price = p
        self.author = a

    def ShowBook(self):
        print("Bid = {0}".format(self.bid))
        print("Bname = {0}".format(self.bname))
        print("Price = {0}".format(self.price))
        print("Author = {0}\n".format(self.author))
    
    def __del__(self):  #Destructor
        print("Object Destroyed")

b1 = Book(101,"AAA",200,"Kk")
b1.ShowBook()


