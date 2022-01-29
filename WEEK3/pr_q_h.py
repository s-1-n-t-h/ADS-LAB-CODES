# priority queues implementation usig queue module of python 

import queue

#size of queue
L = int(input("Size of Queue: "))
#creating the priority queue object

q = queue.PriorityQueue(maxsize=L)

def EnQueue(x):
    if not q.full():
        q.put(x)
        print("\n\nValue {} is En-queued Succesfully.".format(x))
    else:
        print("\n\nQueue is Full with {} items or Over-Flow state".format(L))
        
def DeQueue():
    if not q.empty():
        print("\n\nValue {} is De-queued Succesfully.".format(q.get()))
    else:
        print("\n\nQueue is Empty with {} items or Under-Flow state".format(0))
        
def Peek():
    if not q.empty():
        i = q.get()
        print("\n\nValue {} is at the front of Queue.".format(i))
        q.put(i)
    else:
        print("\n\nQueue is Empty with {} items or Under-Flow state".format(0))
     
def PT():
    print("\n\nThe Elements in the Queue are: ")
    print("[\n")
    l = []
    s = q.qsize()
    for i in range(int(s)):
        i = q.get()
        print(" ",i)
        l.append(i)
    print("\n]")
    for i in range(int(s)):
        q.put(l[i])
           
while(1):
    c = int(input("\n\n1. EnQueue 2. DeQueue 3. Peek 4. Print 5. Exit: "))

    if c==1:
        EnQueue(int(input("\n\nValue: ")))
    elif c==2:
        DeQueue()

    elif c==3:
        Peek()

    elif c==4:
        PT()
    else:
        break
    
        
