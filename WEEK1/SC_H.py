M = int(input("\n\nSize of Hash Table: "))
HT = [[] for i in range(M)]


def HashFn(k):
    return k % M


def insert(value):
    HT[HashFn(value)].append(value)


def PT():
    for i in range(len(HT)):
        print("{} --> {}".format(i,
              " --> ".join([str(HT[i][j]) for j in range(len(HT[i]))])))


def search(value):
    if len(HT[HashFn(value)])==0:
           print("\n\nValue {} is not found.".format(value))
           return
    
    if(value in HT[HashFn(value)]):
            print("\n\nValue {} is found.".format(value))
            return
    else:
        print("\n\nValue {} is not found.".format(value))


def delete(value):

    if(value in HT[HashFn(value)]):
        print("\n\nValue {} is deleted.".format(value))
        HT[HashFn(value)].remove(value)
        return
    else:
        print("\n\nValue {} is not found.".format(value))


while(1):
    c = int(input("\n\n1. Search 2. Insert 3. Delete 4. Print 5. Exit: "))

    if c == 1:
        search(int(input("\nvalue: ")))
    elif c == 2:
        insert(int(input("\nvalue: ")))

    elif c == 3:
        delete(int(input("\nvalue: ")))

    elif c == 4:
        PT()
    else:
        break
