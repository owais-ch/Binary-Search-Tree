'''Given a Binary Tree of size N. Find the sum of all the leaf nodes that are left child of their parent of the given binary tree.

Example 1:

Input:
       1
     /   \
    2     3
Output: 2'''

def leftLeavesSum(root):
    def traversal(root,flag):
        nonlocal total
        if root==None:
            return 0
        elif root.left==None and root.right==None and flag==True:
            total+=root.data
        else:
            traversal(root.left,True)
            traversal(root.right,False)
            
    total=0
    
    traversal(root,False)
    
    return total
