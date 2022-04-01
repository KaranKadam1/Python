# find 2nd,3rd,4rth element in array

data = [40,50,10,20,70]
n = len(data)

max = data[0]
smax = 0
tmax = 0
fmax = 0

for i in range(1,n):
    if(max < data[i]):
        fmax = tmax
        tmax = smax
        smax = max
        max = data[i]
    
    elif(smax < data[i]):
        fmax = tmax
        tmax = smax
        smax = data[i]
    
    elif(tmax < data[i]):
        fmax = tmax
        tmax = data[i]
    
    elif(fmax < data[i]):
        fmax = data[i]

print(max,smax,tmax,fmax)