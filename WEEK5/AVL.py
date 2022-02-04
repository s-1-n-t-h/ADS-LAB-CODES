class Node:
    def __init__(_self_,_value_):
        _self_._value_ = _value_
        _self_._left_= _self_._right_ = None
        _self_._height_ = 1

#This class provides the methods to monitor and operates to satisfy avl tree properties
class AVL:
    # inserts nodes
    def _insert_(_self_,_root_,_key_):
        #verfiying if the tree is empty
        if not _root_:
            return Node(_key_)

        #otherwise
        #let's compare the key with the available root.
        elif _key_ < _root_._value_:
            #point the root's left pointer to newly created node
            _root_._left_ = _self_._insert_(_root_._left_,_key_)

        elif _key_ > _root_._value_:
            #point the root's right pointer to newly created node
            _root_._right_ = _self_._insert_(_root_._right_,_key_)


        #after inserting any new node, the inserted node must affects the height of it's root
        #it's parent height is adjusted by +1 basing on the max height from it's child subtrees  
        _root_._height_ = 1 + max(_self_._getHeight_(_root_._left_),_self_._getHeight_(_root_._right_))

        #now we must check if the root is balanced
        _balance_ = _self_._getBalance_(_root_)

        #conditions for checking un-balacing and fixing it

        #left-left pattern imbalance --> 1 right rotation
        if _balance_ > 1 and _key_ < _root_._left_._value_:
            return _self_._rRotate_(_root_)
        
        #right-right pattern imbalance--> 1 left rotation
        if _balance_ < -1 and _key_ > _root_._right_._value_:
            return _self_._lRotate_(_root_)
        
        # left-right pattern imbalance --> 2 rotations
        # 1st rotate middle node to left
        # lef-right converted to left left after 1 rotation
        # 2nd rotate root to right
        # after one more rotation on the root to the right, new root is returned
        if _balance_ > 1 and _key_ > _root_._left_._value_:
            _root_._left_ = _self_._lRotate_(_root_._left_)
            return _self_._rRotate_(_root_)

        # right - left pattern imbalance --> 2 rotations 
        # 1st rotate middle to the right
        # 2nd rotate root to left
        # after one rotation right left coverts to right right
        # now after one more rotation, now on the root towards left, new root is returned
        if _balance_ < -1 and _key_ < _root_._right_._value_:
            _root_._right_ = _self_._rRotate_(_root_._right_)
            return _self_._lRotate_(_root_)

        #if tree is balanced then just return the existing node as root
        return _root_

        #remember no rotation in any sub tree aftects the balance of rest of the tree in the case of insertion

    #method for returning the height of a node
    #writing this before the next method bcs of calling this in that
    def _getHeight_(_self_,_root_):
        #may be if this method is called when tree is empty
        # then balance factor is 0 bcs not even a single node is present
        if not _root_:
            return 0
        #otherwise
        return _root_._height_

    #method for returning the balace factor for a node
    def _getBalance_(_self_,_root_):
        #may be if this method is called when tree is empty
        # then balance factor is 0 bcs not even a single node is present
        if not _root_:
            return 0
        #otherwise
        return _self_._getHeight_(_root_._left_) - _self_._getHeight_(_root_._right_)
        
    '''Rotating Methods'''

    #rotating the node to the right
    def _rRotate_(_self_,_node_):
        #point middle node right to a temporary pointer
        _temp_ = _node_._left_._right_
        #store the new root inorder to return back
        _root_ = _node_._left_
        #point root's left's right to root
        _node_._left_._right_ = _node_
        #point root's right to middle's right stored in temp
        _node_._left_ = _temp_
        # updating the heights
        _node_._height_ = 1 + max(_self_._getHeight_(_node_._left_),_self_._getHeight_(_node_._right_))
        _root_._height_ = 1 + max(_self_._getHeight_(_root_._left_),_self_._getHeight_(_root_._right_))

        return _root_

    #rotating the node to the left
    def _lRotate_(_self_,_node_):
        #point middle node left to a temporary pointer
        _temp_ = _node_._right_._left_
        #store the new root inorder to return back
        _root_ = _node_._right_
        #point root's right's left to root
        _node_._right_._left_ = _node_
        #point root's left to middle's left stored in temp
        _node_._right_ = _temp_
        # updating the heights
        _node_._height_ = 1 + max(_self_._getHeight_(_node_._left_),_self_._getHeight_(_node_._right_))
        _root_._height_ = 1 + max(_self_._getHeight_(_root_._left_),_self_._getHeight_(_root_._right_))

        return _root_

    #inorder traversal
    def _inorder_(_self_,_root_):
        if _root_:
            _self_._inorder_(_root_._left_)
            print(_root_._value_,end=" ")
            _self_._inorder_(_root_._right_)

        
        

    #method for deleting a node
    def _delete_(_self_,_root_,_key_):
        #if tree is empty return None
        if not _root_:
            return _root_
        #otherwise the key is either equal to root or less than or greater than root's value
        #let's evaluate and perform nescessary operations

        #if key is less than root's value
        elif _key_ < _root_._value_:
            # this comparision if found to be true and node is at left of root
            #there are 3 cases
            # 1 - node may have no further childern --> then just delete the node and point root's left to None
            # 2 - node has only 1 child either to the left or to the right --> then delete the node and point it's child to root's left
            # 3 - node has 2 children --> then find the inorder successor of the node and replace the node with the inorder successor
            _root_._left_ = _self_._delete_(_root_._left_,_key_)
        #otherwise
        #if key is greater than root's value
        elif _key_ > _root_._value_:
            _root_._right_ = _self_._delete_(_root_._right_,_key_)

        # if key is equal to root's value -- there exist 3 cases
        # now this node migh be a leaf node or an internal node
        else: 
            # case 1 - node has n futher children
            # delete the node and return the node as null
            if (_root_._left_ == None) and (_root_._right_ == None):
                _root_ = None
                return _root_
            # case 2 - if node has only 1 child
            # replace the node with it's child
            # child  could be at right or left -- evaluate

            
            if _root_._left_ is None:
                #if left child is null then return right child
                return _root_._right_
            elif _root_._right_ is None:
                #if right child is null then return left child
                return _root_._left_
            #now if the node has both left and right child
            #replace the node with it's inorder successor -- nothing but we change key of to be deleted node with it's 
            #inourder succesor and perform deletion on that node's sub tree recurcively
            else:
                #finding in order successor
                _in_value_ = _self_._getMinValue_(_root_._right_)
                #assigning the inorder succesor's value
                _root_._value_ = _in_value_._value_
                #performing the deletion of the inorder succesor on it's subtree
                _root_._right_ = _self_._delete_(_root_._right_,_in_value_._value_)

            # after all deletion and replacement is done, we return the root after updating heights and rebalancing thre newly formed tree
            #after inserting any new node, the inserted node must affects the height of it's root
        #it's parent height is adjusted by +1 basing on the max height from it's child subtrees
        _root_._height_ = 1 +  max(_self_._getHeight_(_root_._left_), _self_._getHeight_(_root_._right_))

        #now we must check if the root is balanced
        _balance_ = _self_._getBalance_(_root_)

        #conditions for checking un-balacing and fixing it

        #left-left pattern imbalance --> 1 right rotation
        if _balance_ > 1 and _self_._getBalance_(_root_._left_) >= 0:
            return _self_._rRotate_(_root_)

        #right-right pattern imbalance--> 1 left rotation
        if _balance_ < -1 and _self_._getBalance_(_root_._right_) >=0 :
            return _self_._lRotate_(_root_)

        # left-right pattern imbalance --> 2 rotations
        # 1st rotate middle node to left
        # lef-right converted to left left after 1 rotation
        # 2nd rotate root to right
        # after one more rotation on the root to the right, new root is returned
        if _balance_ > 1 and _self_._getBalance_(_root_._left_) < 0:
            _root_._left_ = _self_._lRotate_(_root_._left_)
            return _self_._rRotate_(_root_)

        # right - left pattern imbalance --> 2 rotations
        # 1st rotate middle to the right
        # 2nd rotate root to left
        # after one rotation right left coverts to right right
        # now after one more rotation, now on the root towards left, new root is returned
        if _balance_ < -1 and _self_._getBalance_(_root_._right_) > 0:
            _root_._right_ = _self_.rRotate_(_root_._right_)
            return _self_._lRotate_(_root_)

        #if tree is balanced then just return the existing node as root
        return _root_
            
    def _getMinValue_(_self_,_node_):
        # 2 cases for obtaining in order successor
        # if right subtree exist, then return it's left most node
        # 
        if _node_ is None or _node_._left_ is None :
            return _node_
        
        return _self_._getMinValue_(_node_._left_)
#creating AVL tree class object
Tree = AVL()
#the key for this entire code is tree must be empty
root = None # making tree empty by pointing root it to null or none
#set of nodes to be inserted
while(True):
    print("1. Insertion 2. Deletion 3. Inorder Traversal :", end=" ")
    choice = int(input())
    if choice == 1:
        print('\nElement:', end=" ")
        root = Tree._insert_(root, int(input()))
    elif choice == 2:
        print('\nElement:', end=" ")
        root = Tree._delete_(root, int(input()))
    elif choice == 3:
        print('\nInorder Traversal:', end=" ")
        Tree._inorder_(root)
        print()
    else:
        break

