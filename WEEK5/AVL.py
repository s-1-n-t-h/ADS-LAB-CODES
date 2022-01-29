# defining each node's attributes 
class treeNode(obj):
    def __init__(self,v):
        self.v = v
        self.l = None
        self.r = None
        self.h = 1 
# defining the AVL tree     
class AVLTree(obj):
    def insert(self,r,k):
        # if the tree is empty, insert the node
        if not r:
            return treeNode(k)
        elif k<r.v:
            r.l = self.insert(r.l,k)

