# find largest and smallest number in array

arr = [1,2,3,4,5]
n = len(arr)

max = arr[0]
min = arr[0]
for i in range(1,n):
    if max < arr[i]:
        max = arr[i]
    elif min > arr[i]:
        min = arr[i]

print(f"min={min},max={max}")

