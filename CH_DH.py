p = 1
while(1):
    M = int(input("\n\nSize of Hash Table: "))
    HT = [-1 for i in range(M)]
    n = int(input("\n\nNo.of values: "))

    if(n > M):
        print("\n\nThe Hash Table can't be created.")
    else:
        break


def CalNxtPrime():
    l = [i for i in range(M-1, 0, -1)]
    for i in l:
        if i % 2 != 0:
            p = i
            return


def H1(k):
    return k % M


def H2(k):
    return p - (k % p)

# modified


def insert(value):

    if HT[H1(value)] == -1:
        HT[H1(value)] = value

    else:
        i = (H1(value)+H2(value))%M
        j = 1
        while(HT[i] != -1):
            i = (H1(value)+j*H2(value))%M
            j = j+1
        HT[i] = value


def PT():
    print("\n\nThe hash table is: ", end="")
    print(HT)

# modified


def search(value):
    if HT[H1(value)] == value:
        print("\n\nValue {} is found.".format(value))
        return
    else:
        i = k = H1(value)
        j = 1
    while(1):
        i = (H1(value)+j*H2(value))%M
        j = j+1
        if(HT[k] == HT[i]):
            print("\n\nValue doesn't exist.")
            return

        if HT[i] == -1:
            print("\n\nValue doesn't exist.")
            return

        elif HT[i] == value:
            print("\n\nValue {} is found.".format(value))
            return

# modified


def delete(value):
    if HT[H1(value)] == value:
        print("\n\nValue {} is deleted.".format(value))
        HT[H1(value)] = -1
        return
    else:
        i = k = H1(value)
        j = 1
        while(1):
            i = (H1(value)+j*H2(value))%M
            j = j+1
            if HT[i] == -1:
                print("\n\nValue {} doesn't exist.".format(value))
                return
            elif HT[i] == value:
                print("\n\nValue {} is deleted.".format(value))
                HT[i] = -1
                return


while(1):
    c = int(input("\n\n1. Search 2. Insert 3. Delete 4. Print 5. Exit: "))
    CalNxtPrime()
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