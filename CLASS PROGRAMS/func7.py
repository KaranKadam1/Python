# default parameter concept

def sum(x=0,y=0,z=0):
    return x+y+z

z=sum(10,30,20)
print("sum=",z)

z=sum(10,20)
print("sum=",z)

z=sum(10)
print("sum=",z)

z=sum()
print("sum=",z)