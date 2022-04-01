from heapq import heapify, heappush ,heappop


def kthlargest_heapsort(arr,k):
    heap = []
    heapify(heap)

    for num in arr:
        heappush(heap,num)
        if(len(heap) > k):
            heappop(heap)
               
    return heappop(heap)
        

arr = [22,1,56,4,66]
k = int(input("enter k ="))
pos = kthlargest_heapsort(arr,k)
print(pos)
