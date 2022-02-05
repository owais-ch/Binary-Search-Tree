'''Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3'''

class Solution:
    def maxDepth(self, root) -> int:
        def height(root):
            if root==None:
                return 0
            
            left=height(root.left)
            right=height(root.right)
            
            return max(left,right)+1
        
        return height(root)
