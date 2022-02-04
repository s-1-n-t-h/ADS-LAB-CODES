class Node:
    def __init__(self,value):
        self.value = value
        self.left= self.right = None
        self.height = 1
class AVL:
    def insert(self,root,key):
        if not root:
            return Node(key)
        elif key < root.value:
            root.left = self.insert(root.left,key)
        elif key > root.value:
            root.right = self.insert(root.right,key)
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))
        balance = self.getBalance(root)
        if balance > 1 and key < root.left.value:
            return self.rRotate(root)
        if balance < -1 and key > root.right.value:
            return self.lRotate(root)
        if balance > 1 and key > root.left.value:
            root.left = self.lRotate(root.left)
            return self.rRotate(root)
        if balance < -1 and key < root.right.value:
            root.right = self.rRotate(root.right)
            return self.lRotate(root)
        return root
    def getHeight(self,root):
        if not root:
            return 0
        return root.height
    def getBalance(self,root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)
    def rRotate(self,node):
        temp = node.left.right
        root = node.left
        node.left.right = node
        node.left = temp
        node.height = 1 + max(self.getHeight(node.left),self.getHeight(node.right))
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))
        return root
    def lRotate(self,node):
        temp = node.right.left
        root = node.right
        node.right.left = node
        node.right = temp
        node.height = 1 + max(self.getHeight(node.left),self.getHeight(node.right))
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))
        return root
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.value,end=" ")
            self.inorder(root.right)
    def delete(self,root,key):
        if not root:
            return root
        elif key < root.value:
            root.left = self.delete(root.left,key)
        elif key > root.value:
            root.right = self.delete(root.right,key)
        else: 
            if (root.left == None) and (root.right == None):
                root = None
                return root
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                invalue = self.getMinValue(root.right)
                root.value = invalue.value
                root.right = self.delete(root.right,invalue.value)
        root.height = 1 +  max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rRotate(root)
        if balance < -1 and self.getBalance(root.right) >=0 :
            return self.lRotate(root)
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.lRotate(root.left)
            return self.rRotate(root)
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rRotate_(root.right)
            return self.lRotate(root)
        return root        
    def getMinValue(self,node):
        if node is None or node.left is None :
            return node
        return self.getMinValue(node.left)  
Tree = AVL()
root = None 
while(True):
    print("1. Insertion 2. Deletion 3. Inorder Traversal :", end=" ")
    choice = int(input())
    if choice == 1:
        print('\nElement:', end=" ")
        root = Tree.insert(root, int(input()))
    elif choice == 2:
        print('\nElement:', end=" ")
        root = Tree.delete(root, int(input()))
    elif choice == 3:
        print('\nInorder Traversal:', end=" ")
        Tree.inorder(root)
        print()
    else:
        break

