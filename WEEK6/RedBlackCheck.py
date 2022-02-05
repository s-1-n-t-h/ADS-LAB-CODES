COLOR_BLACK = True
COLOR_RED = False

class Node(object):
    def __init__(self, value=0, parent=None, left=None, right=None, color=COLOR_BLACK):
        self.v = value
        self.p = parent
        self.l = left
        self.r = right
        self.c = color


def rb_tree():
    T = Node(7, None, None, None, COLOR_BLACK)

    l = Node(2, T, None, None, COLOR_RED)
    T.l = l
    r = Node(11, T, None, None, COLOR_RED)
    T.r = r

    ll = Node(1, l, None, None, COLOR_BLACK)
    l.l = ll
    lr = Node(5, l, None, None, COLOR_BLACK)
    l.r = lr

    lrl = Node(4, lr, None, None, COLOR_RED)
    lr.l = lrl

    rl = Node(8, r, None, None, COLOR_BLACK)
    r.l = rl
    rr = Node(14, r, None, None, COLOR_BLACK)
    r.r = rr

    rrr = Node(15, rr, None, None, COLOR_RED)
    rr.r = rrr

    return T

def red_black_tree_check(T):
    return subtree_check(T)

def subtree_check(t):
    if not t:  
        return True, 1

    if not t.p and not t.c:
        return False, 0

    if not t.c: 
        n_blacks = 0
        if (t.l and not t.l.c) or (t.r and not t.r.c):
            return False, -1
    else:  
        n_blacks = 1

    r, n_blacks_r = subtree_check(t.r)
    l, n_blacks_l = subtree_check(t.l)

    return all([r, l, n_blacks_r == n_blacks_l]), n_blacks_r + n_blacks


def main():
    T = rb_tree()
    assert red_black_tree_check(T), "The input tree is not Red-Black"
    print("The input tree is Red-Black")

main()    

