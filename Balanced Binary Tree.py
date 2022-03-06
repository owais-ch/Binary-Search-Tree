''''Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.


Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: true'''
  
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if root==None:
                return 0
            
            left=height(root.left)
            right=height(root.right)
            
            return max(left,right)+1
        
        def traversal(root):
            nonlocal output,tall1,tall2
            if root==None:
                return None
            
            if root.left:
                tall1=height(root.left)
            else:
                tall1=0
                
            if root.right:
                tall2=height(root.right)
            else:
                tall2=0
            print(tall1,tall2)    
            if abs(tall1-tall2)>1:
                output=False
                return 
            
            if root.left:
                traversal(root.left)
                
            if root.right:
                traversal(root.right)
        tall1=0
        tall2=0
        output=True
        traversal(root)
        return output  
