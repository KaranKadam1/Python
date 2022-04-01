# create a class product with members as pid,pname,price and qunatity .
# Add following methods:
# d.Constructor (Support both parameterized and Patameterless)
# e.Destructor
# f.ShowProduct

class Product:
    
    def __init__(self,id,nm,pp,qt): #Parameterized Constructors
        self.pid = id
        self.pname = nm
        self.price = pp
        self.quantity = qt
    
    def ShowProduct(self):
        print("\nPid = {0}".format(self.pid))
        print("Pname = {0}".format(self.pname))
        print("Price = {0}".format(self.price))
        print("Quantity = {0}\n".format(self.quantity))
    
    def __del__(self):  #Destructor
        print("Object Destroyed")

p1 = Product(100,"Pen",2000,5)
p1.ShowProduct()