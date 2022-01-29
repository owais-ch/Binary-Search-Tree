'''Given the root of a binary tree. Check whether it is a BST or not.
Note: We are considering that BSTs can not contain duplicate Nodes.
A BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

Input:
   2
 /    \
1      3
Output: 1 '''


class Solution:
    
    def __init__(self):
            self.list1=[]
    def isBST(self, root):
        
        def traversal(root):
            if root.left:
                traversal(root.left)
                
            self.list1.append(root.data)
            
            if root.right:
                traversal(root.right)
                
        traversal(root)
        
        if self.list1==sorted(self.list1) and len(self.list1)==len(set(self.list1)):
            return True
            
        return False
