'''Given a Binary Tree, write a function to check whether the given Binary Tree is a prefect Binary Tree or not. A Binary tree is Perfect Binary Tree in which all internal nodes have two children and all leaves are at same level.

Example 1:

Input: 
          7
      /  \
     4    9
Output: YES
Explanation: 
As the root node 7 has two children and 
two leaf nodes 4 and 9 are at same level 
so it is a perfect binary tree.'''

class Solution:
    def isPerfect(self,root):
        def height(root):
            if root==None:
                return 0
                
            left=height(root.left)
            right=height(root.right)
            
            return max(left,right)+1
            
        def traversal(root,level):
            nonlocal output
            if root==None:
                output=False
                return 
                
            if level==0:
                pass
            else:
                traversal(root.left,level-1)
                traversal(root.right,level-1)
                
        tall=height(root)
        output=True
        traversal(root,tall-1)
        
        return output
