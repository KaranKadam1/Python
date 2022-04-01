'''
Create a class Shirt with members as sid,sname,type(formal 
etc), price and size(small,large etc) .Add following methods:

j. Constructor (Support both parameterized and parameterless) 
k. Destructor 
l. ShowShirt
m. For each size of shirt price should change by 10%.

(eg. If 1000 is price then small price = 1000, medium = 
1100,large=1200 and xlarge=1300) Use static concept
'''

class Shirt:
    
    gst = 10
    def __init__(self): 
        self.sid = 101
        self.sname = "cottenking"
        self.type = "cotten"
        self.size = "S,M,XL"
        self.price = 1000

        self.s = self.price
        self.m = self.s + (self.s*Shirt.gst/100)
        self.l = self.m + (self.m*Shirt.gst/100)
        self.xl = self.l + (self.l*Shirt.gst/100)

    def ShowShirt(self):
        print("\nShirt id = {0}".format(self.sid))
        print("Shirt name = {0}".format(self.sname))
        print("Type = {0}".format(self.type))
        print("Price = {0}".format(self.price))
        print("Available Size = {0}\n".format(self.size))
        
        print("-----prices according to size------")
        print("S = {0}Rs ,M = {1}Rs ,L = {2}Rs ,XL = {3}Rs".format(self.s,self.m,self.l,self.xl))
    
    def __del__(self):  #Destructor
        print("Object Destroyed\n")

s1 = Shirt()
s1.ShowShirt()