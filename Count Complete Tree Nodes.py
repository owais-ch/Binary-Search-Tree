'''Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. 
It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

 

Example 1:


Input: root = [1,2,3,4,5,6]
Output: 6'''

class Solution:
    def __init__(self):
        self.count=0
    def countNodes(self, root) -> int:
        def traversal(root):
            if root==None:
                return None
            
            if root.left:
                traversal(root.left)
                
            self.count+=1
            
            if root.right:
                traversal(root.right)
                
        traversal(root)
        
        return self.count
        
