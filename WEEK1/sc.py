m = int(input("Enter Size of Table:"))
ht = [[] for i in range(m)]

def HashFn(k):
    return k%m
def insert(value):
    ht[HashFn(value)].append(value)
def search(value):
    if value in ht[HashFn(value)]:
        print("\n\nValue {} found.".format(value))
    else:
        print("Value {} not found.".format(value))
def delete(value):
    if value in ht[HashFn(value)]:
        ht[HashFn(value)].remove(value)
    else:
        print("Value {} not found.".format(value))
def printTable():
    for i in range(len(ht)):
        print("{} --> {}".format(i," --> ".join([str(ht[i][j]) for j in range(len(ht[i]))])))

while(True):
    c = int(input("\n\n1. Search 2. Insert 3. Delete 4. Print 5. Exit: "))

    if c == 1:
        search(int(input("\nvalue: ")))
    elif c == 2:
        insert(int(input("\nvalue: ")))

    elif c == 3:
        delete(int(input("\nvalue: ")))

    elif c == 4:
        printTable()
    else:
        break
