# Create a class shirt with members as sid,sname,type(formal etc),
# price and size(small,large etc)
# Add following methods:
# g.Constructor (Support both parameterized and Patameterless)
# h.Destructor
# i.ShowShirt

class Shirt:

    def __init__(self,id,nm,tp,pp,sz): 
        self.sid = id
        self.sname = nm
        self.type = tp
        self.price = pp
        self.size = sz

    def ShowShirt(self):
        print("\nShirt id = {0}".format(self.sid))
        print("Shirt name = {0}".format(self.sname))
        print("Type = {0}".format(self.type))
        print("Price = {0}".format(self.price))
        print("Size = {0}\n".format(self.size))
    
    def __del__(self):  #Destructor
        print("Object Destroyed")
        
s = Shirt(103,"SSS","Cotten",2000,"XL")
s.ShowShirt()