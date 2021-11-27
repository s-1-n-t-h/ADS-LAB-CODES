d = {}

def delete():
    if not d:
        print("Empty!")
        return
    
    x = input("key: ")
    if x not in d:
        print("key doesn't exist!")
        return
    del d[x]
    print(d)
def insert():
    x = input("key: ")
    y = input("value: ")
    d[x] = y
    print(d)
def update_():
    x = input("key: ")
    if x not in d:
        print("key doesn't exist!")
        return
    y = input("value: ")
    d[x] = y
    print(d)
def print_d():
    print(d)
def search():
    x = input("key: ")
    print("value of key",x,"is: ",d[x])
while True:
    print("1.insert 2.update 3.delete 4.print 5.search")
    n = int(input("choice: "))
    if n==1:
        insert()
    elif n==2:
        update_()
    elif n==3:
        delete()
    elif n==4:
        print_d()
    elif n==5:
        search()
    else:
        break


    
