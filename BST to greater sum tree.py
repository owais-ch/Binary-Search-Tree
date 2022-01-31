'''Given a BST, transform it into greater sum tree where each node contains sum of all nodes greater than that node.

Example 1:

Input:
           2
         /    \
        1      6
              /  \
             3    7
Output: 18 16 13 7 0
Explanation:
Every node is replaced with the 
sum of nodes greater than itself. 
The resultant tree is:
               16
             /    \
           18       7
                  /   \
                 13    0'''


class Solution:
    def transformTree(self, root):
        total_sum=0
        
        def traversal_sum(root):
            nonlocal total_sum
            
            total_sum+=root.data
            
            if root.left:
                traversal_sum(root.left)
                
            if root.right:
                traversal_sum(root.right)
                
            
        traversal_sum(root)
        
        def traversal(root):
            nonlocal total_sum
            if root.left:
                traversal(root.left)
                
            total_sum=total_sum-root.data
            root.data=total_sum
            
            if root.right:
                traversal(root.right)
                
            return root
            
        
        return traversal(root)
