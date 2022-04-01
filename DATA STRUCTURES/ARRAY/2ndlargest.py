# find second largest element in array without sorting


data = [40,50,10,20,70]
n = len(data)

max = data[0]
smax = data[0]

for i in range(1,n):
    if(max < data[i]):
        smax = max
        max = data[i]
    
    elif(smax < data[i]):
        smax = data[i]

print(max,smax)
print(f"Second largest element in array= {smax}")