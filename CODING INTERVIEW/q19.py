# find top two maximum number in array

array = [1,2,3,4,5]
n = len(array)

max = array[0]
smax = 0

for i in range(1,n):
    if max < array[i]:
        smax = max
        max = array[i]
    elif smax<array[i]:
        smax = array[i]

print(f"Top two maximum number in array are={max} and {smax}")    

