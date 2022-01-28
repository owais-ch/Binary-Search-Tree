'''Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true'''

class Solution(object):
    def __init__(self):
        self.list1=[]
    def isValidBST(self, root):
        def traversal(root):
            if root.left:
                traversal(root.left)
                
            self.list1.append(root.val)
            
            if root.right:
                traversal(root.right)
                
        traversal(root)
        
        for i in range(-1,-len(self.list1),-1):
            if self.list1[i]<=self.list1[i-1]:
                return False
        return True
