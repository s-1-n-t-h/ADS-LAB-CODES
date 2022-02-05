from heapq import merge
 
# function for meging k arrays
def mergeK(arr, k):
    l = []
    for i in range(k):
        l = list(merge(l, arr[i]))
    return l
 
print("Enter no of arrays: ",end=" ")
n = int(input())
sortedList = []
for i in range(n):
    print("Input Sorted array no {}: ".format(i+1),end=" ")
    sortedList.append(list(map(int, input().split())))
 
l = mergeK(sortedList,n)
 
print(l)
