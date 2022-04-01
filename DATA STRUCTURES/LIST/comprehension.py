# List Comprehension -->Compress the code

data=[10,20,30,40,50,60]
new_data = [x*2 for x in data]
print(new_data)


new_data = [x**3 for x in data]
print(new_data)


new_data = {x:x**3 for x in data}
print(new_data)


data = {1:21,2:34,3:45}
mydata = [x for x in data]
mydata = [x for x in data.values()]
mydata = [x for x in data.keys()]
mydata = [x+y for x,y in data.items()]
print(mydata)

odd_data=[]
for x in data:
    if(x%2 != 0):
        odd_data.append(x)
print(odd_data)

odd_data=[x for x in data if(x%2 != 0)]
print(odd_data)
        
mydata = {y:x for y,x in data.items()}
print(mydata)
