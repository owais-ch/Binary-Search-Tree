'''Given a BST and a number X, find Ceil of X.
Note: Ceil(X) is a number that is either equal to X or is immediately greater than X.

Example 1:

Input:
      5
    /   \
   1     7
    \
     2 
      \
       3
X = 3
Output: 3
Explanation: We find 3 in BST, so ceil
of 3 is 3.'''

class Solution:
    def findCeil(self,root, inp):
        def traversal2(root):
            nonlocal f,count
            if root==None:
                return None
                
            
            
            if root.left:
                traversal2(root.left)
                
            if root.key>=inp and count==0:
                f=root.key
                count+=1
            
            if root.right:
                traversal2(root.right)
                
        f=-1
        count=0
        
        traversal2(root)
        
        return f
