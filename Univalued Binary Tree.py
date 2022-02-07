'''A binary tree is uni-valued if every node in the tree has the same value.

Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.

Example 1:
  
Input: root = [1,1,1,1,1,null,1]
Output: true'''


class Solution:
    def isUnivalTree(self, root) -> bool:
        def traversal(root):
            nonlocal output
            if root==None:
                return None
            elif root.left and root.right:
                if root.val!=root.left.val or root.val!=root.right.val:
                    output=False
                    return 
            elif root.left:
                if root.val!=root.left.val:
                    output=False
                    return 
            elif root.right:
                if root.val!=root.right.val:
                    output=False
                    return 
            
            if root.left:
                traversal(root.left)
                
            if root.right:
                traversal(root.right)
        
        output=True        
        
        traversal(root)
        
        return output
