# Remove the chracters of odd index values in a string
'''
inp=hello
out=hlo

'''

string = input("enter a string= ")
result= ""

for i in range(len(string)):
    if i%2 == 0:
        result = result + string[i]
print(result)
