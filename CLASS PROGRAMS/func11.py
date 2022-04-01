# function with var num of arguments
# *a represents we are passing multiple arg

def sum(*a):
    # print(a)
    s = 0
    for x in a:
        s = s+x
    return s

z = sum(10,20,30,40,50)
print(z)
z = sum(10,20,30,40,50,60,70)
print(z)
z = sum(10,20)
print(z)
