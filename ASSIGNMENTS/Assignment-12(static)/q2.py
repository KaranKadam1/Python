'''
Create a class Product with members as pid,pname,price and 
quantity .Add following methods: 
e. Constructor (Support both parameterized and parameterless) 
f. Destructor 
g. ShowProduct 
h. Add static member discount. 
i. Provide methods for applying discount on price of product
'''
class Product:

    discount = 0.1  #20% 

    def __init__(self,id=0,nm="",pp=0,qt=0): #Constructors
        self.pid = id
        self.pname = nm
        self.price = pp
        self.quantity = qt
    
    def applyDiscount(self):
        discount = self.price*self.quantity*Product.discount
        total = self.price*self.quantity-discount
        return total
    
    # def ShowProduct(self):
    #     print("\nPid = {0}".format(self.pid))
    #     print("Pname = {0}".format(self.pname))
    #     print("Price = {0} Rs".format(self.price))
    #     print("Quantity = {0}".format(self.quantity))
    
    def __del__(self):  #Destructor
        print("Object Destroyed\n")

p1 = Product(101,"laptop",2000,2)
p1.applyDiscount()
print("total=",p1.applyDiscount())