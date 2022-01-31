class BST:
    def __init__(self,key):
        self.lchild = None
        self.key = key
        self.rchild = None
    # runs without accepting duplicates
    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if self.key  > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)
    # search algorithm
    def search(self,data):
        if self.key == data:
            print("Found")
            return
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Not Found")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Not Found")
    
    # preorder traversal

    def preorder(self):
        print(self.key,end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
        

    # postorder traversal

    def postorder(self):
        
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key, end=" ")
        
    # inorder traversal

    def inorder(self):

        if self.lchild:
            self.lchild.inorder()
        print(self.key, end=" ")
        if self.rchild:
            self.rchild.inorder()

    def delete(self,data,curr):
        if self.key is None:
            print("Empty Tree")
            return
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data,curr)
            else:
                print("Not Found")
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data,curr)
            else:
                print("Not Found")
        else:
            if self.lchild is None:
                temp = self.rchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp
            
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key,curr)
        return self
        
          
def count(node):
    if node is None:
        return 0
    return 1 + count(node.lchild)+ count(node.rchild)
        

root = BST(10)

l = [11,12]

for i in l:
    root.insert(i) 
    
root.search(1)
print('\npreorder')
root.preorder()
print('\npostorder')
root.postorder()
print('\ninorder')
root.inorder()
     
root.delete(3,10)
root.preorder()
root.delete(10,10)
print()
root.preorder()

