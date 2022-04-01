'''
lambda function is anonymous function.in this function defination declare with function call.
it reduces num of lines of code and saves time.
eg. result= lambda x: x*x*x
    print(result)


'''
result= lambda x: x*x*x
print(result(10))

z = lambda x,y: x+y
print(z(10,20))
# r= z(10,20)
# c= result(r)
# print(c)


# using collection of data
data = [4,3,1,6,7]
final=[]

result = lambda x:x*x*x

for x in data:
    final.append(result(x))
print(final)

# map function
result = lambda x:x*x*x
data = [4,3,1,6,7]
final=list(map(result,data))
print(final)


# even odd
result = lambda x: x%2==0
data = [4,3,1,6,7]
final = list(map(result,data))
print(final)

# filter method
result = lambda x: x%2==0
data = [4,3,1,6,7]
final = list(filter(result,data))
print(final)
