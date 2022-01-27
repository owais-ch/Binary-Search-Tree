'''Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:

Input: root = [1,null,2,3]
Output: [1,3,2]'''


class Solution:
    def __init__(self):
        self.list1=[]
        
    def inorderTraversal(self, root):
        if root==None:
            return self.list1
        if root.left:
            self.inorderTraversal(root.left)
            
        self.list1.append(root.val)
        
        if root.right:
             self.inorderTraversal(root.right)
                
        return self.list1
        
