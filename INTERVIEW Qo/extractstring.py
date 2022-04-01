'''
given a string extract digits from it and print it.

eg:["1","A","2","E","3"]
output : 1,2,3
1A2E3

'''
result = ""
data= input("Enter the string=")
for x in data:
    if(x.isdigit()):
        result += x
print(result)