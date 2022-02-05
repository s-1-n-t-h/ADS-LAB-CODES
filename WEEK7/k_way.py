from heapq import merge
 
# function for meging k arrays
def mergeK(arr, k):
    l = []
    for i in range(k):
        l = list(merge(l, arr[i]))
    return l
 

sortedList =[[2, 6],
    [ 10,11],
    [23, 34, 90],[7,21,38,93]]
k = 4
 
l = mergeK(sortedList, k)
 
print(l)