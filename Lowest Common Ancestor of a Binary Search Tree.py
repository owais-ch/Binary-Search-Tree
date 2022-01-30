'''Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both 
  p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.'''



class Solution:
    def __init__(self):
        self.rootz=None
    def lowestCommonAncestor(self, root1, p, q) -> 'TreeNode':
        def traversal(root):
            if p.val<=root.val and q.val>=root.val:
                self.rootz=root
                print(self.rootz.val)
            elif p.val>=root.val and q.val<=root.val:
                self.rootz=root
           
            if root.left:
                if self.rootz!=None:
                    return self.rootz
                traversal(root.left)
                if self.rootz!=None:
                    
                    return self.rootz
                
            if root.right:
                if self.rootz!=None:
                    
                    return self.rootz
                traversal(root.right)
                if self.rootz!=None:
                    
                    return self.rootz
                
            
            
        return traversal(root1)
