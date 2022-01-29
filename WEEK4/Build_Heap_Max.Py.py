n = 0#size of list

def heapify(L,i):
    
    s = i # node to be heapified
    l = 2*i + 1 #left child node
    r = 2*i + 2 #right child node
    
    
    if(l<n and L[l] > L[s]): #checking if left child is smaller than it's parent
        s = l
    
    if(r<n and L[r]>L[s]): #check if right child is smaller than smallest
        s = r
    
    if( s != i): #if smallest is not parent
        swap(i,s) #swapping for satisfying the property
        
        #recursively heapify the effected sub tree
        heapify(L,s)

def BuildHeap(L):
    
    for i in range(n,-1,-1):
        heapify(L,i)
        
    
def swap(i,s):
    L[i],L[s] = L[s],L[i]   
    
     
L = list(map(int,input("Elements: ").split(" ")))

#calculate the size of list using -- (L.__sizeof__()/L[0].__sizeof__()) or
n =  len(L)

print("List or Array reprsentation Before Build-Heap: ",L)

BuildHeap(L)
print("\n")
print("List or Array reprsentation After Build-Heap: ",L)