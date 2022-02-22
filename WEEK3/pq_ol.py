n = int(input("No of Nodes: "))
ol = []
for i in range(n):
    ol.append([int(input("Enter node "+str(i)+": "))])

queue = []

def dequeue(value):
    if not queue:
        print("queue is Under Flow !")
    else:
        print(queue.remove(value))
def enqueue(value):
    if(len(queue)==n):
        print("queue is Over Flow !")
        return
    else:
        queue.append(value)


for i in range(len(ol)):
    enqueue(ol[i][0])
print('ordered list is: ',ol)

while True:
    print("Select 1.Enqueue 2.Dequeue 3.Print 4.front element 5.rear element")
    choice = int(input("Enter the choice: "))
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        print(queue)
    elif choice == 4:
        print("The element at the front is: ", queue[0])
    elif choice == 5:
        print("The element at the rear is: ", queue[-1])
