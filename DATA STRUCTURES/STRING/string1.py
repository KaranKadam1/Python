data = "Karan Kadam"
print(data)

for x in data:
    print(x,end="  ")

'''
output= K  a  r  a  n     K  a  d  a  m  
'''

print(len(data))#inbuilt method for length

count = 0     #len without using inbuilt method
for x in data:
    count += 1
print("length of string=",count)

