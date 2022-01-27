'''Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
  
Input: root = [5,3,6,2,4,null,7], k = 9
Output: true'''

class Solution:
    def __init__(self):
        self.dict1=dict()
    def findTarget(self, root, k):
        def traversal(root):
            if root.left:
                traversal(root.left)
                
            self.dict1[root.val]=1
            
            if root.right:
                traversal(root.right)
                
        traversal(root)        
        
        length=len(self.dict1)
        
        for i in self.dict1:
            if k-i in self.dict1 and k-i!=i:
                return True
            
        return False
