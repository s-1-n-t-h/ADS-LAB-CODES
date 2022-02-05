queue = []
def dequeue():
    if not queue:
        print("queue is Under Flow !")
    else:
        print(queue.pop(0))
def enqueue():
    if(len(queue)==n):
        print("queue is Over Flow !")
        return
    else:
        queue.append(int(input("Enter the element:")))
n = int(input("Enter the size of queue: "))

while True:
    print("Select 1.Enqueue 2.Dequeue 3.Print 4.front element 5.rear element")
    choice = int(input("Enter the choice: "))
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        print(queue)
    elif choice==4:
        print("The element at the front is: ",queue[0])
    elif choice==5:
        print("The element at the rear is: ",queue[-1])
    
        
