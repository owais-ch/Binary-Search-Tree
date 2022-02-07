'''Given a Binary Tree of size N , where each node can have positive or negative values. Convert this to a tree where each node contains the sum of the left
and right sub trees of the original tree. The values of leaf nodes are changed to 0.

Example 1:

Input:
             10
          /      \
        -2        6
       /   \     /  \
     8     -4   7    5

Output:
            20
          /    \
        4        12
       /  \     /  \
     0     0   0    0'''

class Solution:
    def toSumTree(self, root) :
        def traversal(root):
            nonlocal total_sum
            if root==None:
                return None
                
            if root.left:
                traversal(root.left)
                
            if root.right:
                traversal(root.right)
                
            total_sum+=root.data
            
        def traversal2(root):
            nonlocal total_sum
            if root==None:
                return None
            
            traversal(root)
            
            root.data=total_sum-root.data
            
            total_sum=0
            
            if root.left:
                traversal2(root.left)
                
            if root.right:
                traversal2(root.right)
            
        total_sum=0
        traversal2(root)
        return root
