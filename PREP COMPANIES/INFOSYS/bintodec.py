# convert binary to decimal

num = int(input("enter binary="))

binary_str=str(num)
decimal =0

for i in range(len(binary_str)):
    decimal += int(binary_str[i])*(2**(len(binary_str)-i-1))
print("decimal=",decimal)


# convert decimal to binary

num = int(input("enter decimal="))

string =""
while(num>1):
    string += str(num%2)
    num = num//2
else:
    string += str(num)

binary = string[::-1]
print(binary)