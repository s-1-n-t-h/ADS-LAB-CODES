m = int(input("Enter table size: "))
ht = [-1 for i in range(m)]
p = 1

def hf(k):
    return k % m

def CalPrime():
    if m-1 == 2:
        p = 2
        return
    else:
        l = [i for i in range(m-1,1,-1)]
        for i in l:
            for j in range(2,m//2+1):
                if i%j==0:
                    break
            else:
                p = i

def gf(k):
    CalPrime()
    return p-(k%p)

def insert(value):
    if ht[hf(value)] == -1:
        ht[hf(value)] = value
    else:
        k = 1
        i = (hf(value)+gf(value)*k)%m
        while(ht[hf(i)] != -1):
            if hf(i) == hf(value):
                print("\n\nTable is Full")
                return
            k = k+1
        ht[hf(i)] = value


def delete(value):
    if value in ht:
        for i in range(len(ht)):
            if ht[i] == value:
                ht[i] = -1
                print("\n\nValue {} deleted.".format(value))
    else:
        print("\n\nValue {} not found".format(value))


def printTable():
    for i in range(len(ht)):
        print("{} --> {}".format(i, ht[i]))


def search(value):
    if value in ht:
        print("\n\nValue {} found.".format(value))
    else:
        print("\n\nValue {} not found.".format(value))


while(1):
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
