# find second and fourth smallest element in unsorted array

data = [3,2,8,4,9,5]
n = len(data)

min = 100000
    
min = min
smin = min
tmin = min
fmin = min
    
for i in range(0,n):
    if(data[i] < min):
        fmin = tmin
        tmin = smin
        smin = min
        min = data[i]
    
    elif(data[i] < smin):
        fmin = tmin
        tmin = smin
        smin = data[i]
    
    elif(data[i] < tmin):
        fmin = tmin
        tmin = data[i]
    
    elif(data[i] < fmin):
        fmin = data[i]

print(smin,fmin)


