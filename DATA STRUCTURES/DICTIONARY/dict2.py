data = {101:"Atul",104:"Rashmi",106:"Seema",110:"Tejas",101:"Shruti"}
print(data.get(101))

'''
if(111 in data):
    print(data[111])
else:
    print("111 not present")
'''
# get method returns none if key is not found
# we can specify what has to be return if we dont want None
print(data.get(111,-1)) #if not present print -1
print(data.get(111,"Not found")) #if not present print Not found

# data.clear() =Not found
# del data[101] 
# del data={}

print(len(data))

# set-> varient of dictionary which contains only keys,no values
# we cannot modify the key(Immutable)
# keys data type must be immutable

# different immutable datatypes in data= Tuple,String,Numeric(int,float,compex)

x = 10
y = 10
print(f"loc x={id(x)} and loc y={id(y)}") #if x and y has same values then it points to the same location

c = 10+20j
print(c,type(c)) #complex


# Data types in Python
'''
1.Numeric(int,float,complex)
2.String
3.List
4.Tuple
5.Dictionary
6.Set
'''





