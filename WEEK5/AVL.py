#This class provides the proper structure for any node in the avl tree
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
            _root_._left_ = _self_._lRotate(_root_._left_)
            return _self_._rRotate(_root_)

        # right - left pattern imbalance --> 2 rotations 
        # 1st rotate middle to the right
        # 2nd rotate root to left
        # after one rotation right left coverts to right right
        # now after one more rotation, now on the root towards left, new root is returned
        if _balance_ < -1 and _key_ < _root_._right_.value_:
            _root_._right_ = _self_.rRotate(_root_._right_)
            return _self_._lRotate(_root_)

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
        #point root's left's right to root
        _node_._left_._right_ = _node_
        #point root's right to middle's right stored in temp
        _node_._right_ = _temp_

    #rotating the node to the left
    def _lRotate_(_self_,_node_):
        #point middle node leftt to a temporary pointer
        _temp_ = _node_._right_._left_
        #point root's right's leftt to root
        _node_._right_._left_ = _node_
        #point root's leftt to middle's left stored in temp
        _node_._left_ = _temp_

    #inorder traversal
    def _inorder_(_self_,_root_):
        if _root_:
            _self_._inorder_(_root_._left_)
            print(_root_._value_,end=" ")
            _self_._inorder_(_root_._right_)


#creating AVL tree class object
Tree = AVL()
#the key for this entire code is tree must be empty
root = None # making tree empty by pointing root it to null or none
#set of nodes to be inserted
nodes = [5,3,8,1,4,6,9,2,7]
#inserting nodes
for n in nodes:
    root = Tree._insert_(root,n)
#printing inorder traversal
Tree._inorder_(root)