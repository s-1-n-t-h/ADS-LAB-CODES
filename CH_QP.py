
while(1):
    M = int(input("\n\nSize of Hash Table: "))
    HT = [-1 for i in range(M)]
    n = int(input("\n\nNo.of values: "))

    if(n > M):
        print("\n\nThe Hash Table can't be created.")
    else:
        break


def HashFn(k):
    return k % M


def ReHashFn(k):
    return k % M


def insert(value):

    if HT[HashFn(value)] == -1:
        HT[HashFn(value)] = value

    else:
        k = 1
        i = value + k*k
        k = k+1
        while(HT[ReHashFn(i)] != -1):
            i = value + k*k 
            k = k + 1
        HT[HashFn(i)] = value


def PT():
    print("\n\nThe hash table is: ", end="")
    print(HT)


def search(value):
    if HT[HashFn(value)] == value:
        print("\n\nValue {} is found.".format(value))
        return
    else:
        k = i = value
    while(1):
        i = i+1
        if(ReHashFn(k) == HashFn(i)):
            print("\n\nValue doesn't exist.")
            return

        if HT[ReHashFn(i)] == -1:
            print("\n\nValue doesn't exist.")
            return

        elif HT[ReHashFn(i)] == value:
            print("\n\nValue {} is found.".format(value))
            return


def delete(value):
    if HT[HashFn(value)] == value:
        print("\n\nValue {} is deleted.".format(value))
        HT[HashFn(value)] = -1
        return
    else:
        k = 1
        while(1):
            i = value
            i = i + k*k
            k = k+1
            if HT[ReHashFn(i)] == -1:
                print("\n\nValue {} doesn't exist.".format(value))
                return
            elif HT[ReHashFn(i)] == value:
                print("\n\nValue {} is deleted.".format(value))
                HT[ReHashFn(i)] = -1
                return


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
