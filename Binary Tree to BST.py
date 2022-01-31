'''Given a Binary Tree, convert it to Binary Search Tree in such a way that keeps the original structure of Binary Tree intact.
 

Example 1:

Input:
      1
    /   \
   2     3
Output: 1 2 3'''

class Solution:
    def __init__(self):
        self.list1=[]
        self.count=-1
    def binaryTreeToBST(self, root):
        def traversal(root):
            
            if root.left:
                traversal(root.left)
                
            self.list1.append(root.data)
            
            if root.right:
                traversal(root.right)
                
        traversal(root)
        
        
        self.list1.sort()
        
        def traversal2(root):
            
            if root.left:
                traversal2(root.left)
            
            self.count+=1    
            root.data=self.list1[self.count]
            
            if root.right:
                traversal2(root.right)
                
            return root
                
            
        return traversal2(root)
