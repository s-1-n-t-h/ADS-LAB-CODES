class Node:
    def __init__(self, key=0, parent=None, left=None, right=None, color=1):
        self.key = key
        self.l = left
        self.r = right
        self.color = color
        self.p = parent


root = Node(7, None, None, None, 0)
l = Node(2, root, None, None, 1)
r = Node(11, root, None, None, 1)
root.l = l
root.r = r

ll = Node(1, l, None, None, 1)
lr = Node(5, l, None, None, 1)
l.l = ll
l.r = lr

rl = Node(8, r, None, None, 1)
rr = Node(14, r, None, None, 1)
r.l = rl
r.r = rr


def verify(obj):
    # property 1 -- root should be black and consecutives should be alternative
    if obj == None:
        return
    if obj.color == 0:
        print("Node is black")
    else:
        print("Node is red")
    verify(obj.l)
    verify(obj.r)

# property 2 -- every path from root to leaf should have the same number of black nodes


bcountl = 0
bcountr = 0


def countblack(obj):
    #global bcountl, bcountr
    if obj == None:
        return
    if obj.l.color == 0 and obj.l is None:
        global bcountl
        bcountl += 1
        countblack(obj.l)
    if obj.r.color == 0 and obj.r is None:
        global bcountr
        bcountr += 1
        countblack(obj.r)
    print(bcountl, bcountr)
    if bcountl == bcountr:
        print("Same number of black nodes on left and right")
    else:
        print("Different number of black nodes on left and right")



verify(root)
countblack(root)
