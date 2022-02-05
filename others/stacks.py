stack = []
def pop_operation():
    if not stack:
        print("stack is in Under Flow state !")
    else:
        print(stack.pop())
def push():
    if(len(stack)==n):
        print("stack is in Over Flow state !")
        return
    else:
        stack.append(int(input("Enter the element:")))
def top():
    print("The element at the top of the stack is: ",stack[-1])
n = int(input("Enter the size of stack: "))

while True:
    print("Select 1.Push 2.Pop 3.Print 4.top element of the stack: ")
    choice = int(input("Enter the choice: "))
    if choice==1:
        push()
    elif choice==2:
        pop_operation()
    elif choice==3:
        print(stack)
    elif choice==4:
        top()
        
        
            
                   
