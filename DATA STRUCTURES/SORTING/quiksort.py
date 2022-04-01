
def quiksort(arr):
    
    n = len(arr)
    if(n < 1):
        return arr
    else:
        pivot = arr.pop()
    
    item_lower = []
    item_greater = []

    for item in arr:
        if item > pivot:
            item_greater.append(item)
        else:
            item_lower.append(item)

    return quiksort(item_lower) + [pivot] + quiksort(item_greater)

arr = [55,6,99,4,1,9]
arr = quiksort(arr)
print(arr)