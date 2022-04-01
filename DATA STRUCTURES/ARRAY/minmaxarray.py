#find MinMax element in array

data = [40,50,10,20,70]
n = len(data)

max = data[0]
min = data[0]

for i in range(1,n):
    if(max < data[i]):
        max = data[i]
    
    if(min > data[i]):
        min = data[i]

print(f"Min element in array is {min}")
print(f"Max element in array is {max}")
