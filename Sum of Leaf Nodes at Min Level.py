'''Given a Binary Tree of size N, find the sum of all the leaf nodes that are at minimum level of the given binary tree.
Example 1:

Input: 
         1
        /  \
       2    3
     /  \     \
    4    5     8 
  /  \ 
 7    2      
Output:
sum = 5 + 8 = 13'''

class Solution:
    def minLeafSum(self,root):
        def height(root):
            if root==None:
                return 0
                
            left=height(root.left)
            right=height(root.right)
            
            return max(left,right)+1
            
        def traversal(root,level):
            nonlocal total
            if root==None:
                return None
                
            if level==0:
                if root.left==None and root.right==None:
                    total+=root.data
                    
            else:
                traversal(root.left,level-1)
                traversal(root.right,level-1)
                
        tall=height(root)
        
        total=0
        
        for i in range(tall):
            traversal(root,i)
            if total!=0:
                return total
