'''Given the root of a binary tree, return the sum of values of nodes with an even-valued grandparent. If there are no nodes with an even-valued grandparent, return 0.

A grandparent of a node is the parent of its parent if it exists.

Example 1:

Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.'''

class Solution:
    def sumEvenGrandparent(self, root) -> int:
        def traversal(root):
            nonlocal total_sum
            if root==None:
                return None
            if root.val%2==0 and root.left:
                
                if root.left.left:
                    total_sum+=root.left.left.val
                if root.left.right:
                    
                    total_sum+=root.left.right.val
            if root.val%2==0 and root.right:
                if root.right.right:
                    total_sum+=root.right.right.val
                if root.right.left:
                    total_sum+=root.right.left.val
            
            if root.left:
                traversal(root.left)
                
            if root.right:
                traversal(root.right)
                    
            return total_sum
        total_sum=0
        
        traversal(root)
        
        return total_sum
