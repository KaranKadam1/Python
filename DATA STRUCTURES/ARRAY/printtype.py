x = 10
f = 34.55
str1 = "Hello"

print(x,f,str1)
print("x = ",x,"f = ",f,"str = ",str1)
print("x = "+ str(x) +"f = " + str(f) + "str = "+str(str1))

#C style
print("x = {0},f = {1},str = {2}".format(x,f,str1))
print("x = %d,f = %f,str = %s"%(x,f,str1))
print("x = %10d,f = %f,str = %s"%(x,f,str1))

print("x = %10d,f = %-10.3f,str = %s"%(x,f,str1)) #-1 for left align


print("|    Name        |      Price     |     Decription     |")
print("|------------------------------------------------------|")
print("%10d  %20f  %15s"%(x,f,str1))




