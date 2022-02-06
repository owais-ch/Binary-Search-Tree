'''Given the root of a binary tree, return the leftmost value in the last row of the tree.

Example 1:
  
Input: root = [2,1,3]
Output: 1'''

class Solution:
    def __init__(self):
        self.list1=[]
    def findBottomLeftValue(self, root) -> int:
        def height(root):
            if root==None:
                return 0
            
            left=height(root.left)
            right=height(root.right)
            
            return max(left,right)+1
        
        def traversal(root,level):
            if root==None:
                return None
            
            if level==1:
                if root.left:
                    self.list1.append(root.left.val)
                    return 
                elif root.right:
                    
                    self.list1.append(root.right.val)
                    return
                
                    
            else:
                traversal(root.left,level-1)
                traversal(root.right,level-1)
        
        if root.left==None and root.right==None:
            return root.val
        
        tall=height(root)
        
        traversal(root,tall-1)
        
        if self.list1==[]:
            return None
        return self.list1[0]
