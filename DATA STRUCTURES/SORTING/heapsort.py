from heapq import heapify,heappop,heappush

def heapsort(arr):

    heap = []
    heapify(heap)

    for i in arr:
        heappush(heap,i)
    
    sorted_order = []
    while heap:
        sorted_order.append(heappop(heap))
    return sorted_order

arr = [55,6,99,4,1,9]
sorted = heapsort(arr)
print(sorted)