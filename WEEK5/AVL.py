<<<<<<< Updated upstream
class treeNode(object):
    def __init__(self,value):
        self.value = value
        self.l = None; self.r = None
        self.h = 1

class AVLTree(object):
    
    def insert(self,root,key):
        
        if not root:
            return treeNode(key)
        elif key < root.value:
            root.l = self.insert(root.l,key)
        else:
            root.r = self.insert(root.r,key)
            
        root.h = 1 + max(self.getHeight(root.l),self.getHeight(root.r))

        b = self.getBal(root)
        
        if b > 1 and key < root.l.value:
            return self.rRotate(root)
        if b < -1 and key > root.r.value:
            return self.lRotate(root)
        if b > 1 and key > root.l.value:
            root.l = self.lRotate(root.l)
            return self.rRotate(root)
        if b < -1 and key < root.r.value:
            root.r = self.rRotate(root.r)
            return self.lRotate(root)
        return root
    
    def lRotate(self,z):
        y = z.r
        T2 = y.l
        
        y.l = z
        z.r = T2
        
        z.h = 1 + max(self.getHeight(z.l),self.getHeight(z.r))
        y.h = 1 + max(self.getHeight(y.l),self.getHeight(y.r))
        
        return y
            
    def rRotate(self,z):
        y = z.l
        T3 = y.r
        
        y.r = z
        z.l = T3
        
        z.h = 1 + max(self.getHeight(z.l),self.getHeight(z.r))
        y.h = 1 + max(self.getHeight(y.l),self.getHeight(y.r))
        
        return y
    
    def getHeight(self,root):
        if not root:
            return 0
        return root.h
    
    def getBal(self,root):
        if not root:
            return 0
        return self.getHeight(root.l) - self.getHeight(root.r)
        
    def preOrder(self,root):
        if not root:
            return
        print("{0}".format(root.value),end=" ")
        self.preOrder(root.l)
        self.preOrder(root.r)
        
        
if __name__ == "__main__":
    Tree = AVLTree()
    root = None
    
    root = Tree.insert(root,1)
    root = Tree.insert(root,2)
    root = Tree.insert(root,3)
    root = Tree.insert(root,4)
    root = Tree.insert(root,5)
    root = Tree.insert(root,6)
    
    print("PreOrder Traversal of the constructed AVL Tree is: ",end="")
    Tree.preOrder(root)
    print()
=======
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
        else:
            r.r = self(r.r,k)

        # update the height of the node

        r.h = 1 + max(self.getHeight(r.l),self.getHeight(r.r))

        # if the node is unbalanced, rotate the tree

        bf = self.getBal(r)

        #conditons for verifying balance factor

        if bf > 1 and k < r.l.v:
            return self.rRotate(r)
        if bf < -1 and k > r.r.v:
            return self.lRotate(r)
        if bf > 1 and k > r.l.v:
            r.l = self.lRotate(r.l)
            return self.rRotate(r)
        if bf < -1 and k < r.r.v:
            r.r = self.rRotate(r.r)
            return self.lRotate(r)
        return root

if __name__ == "__main__":
    Tree = AVLTree()
    root = None

    root = Tree.insert(root,1)
>>>>>>> Stashed changes
