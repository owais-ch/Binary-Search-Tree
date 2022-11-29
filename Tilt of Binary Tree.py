'''Given a binary tree of size N+1, your task is to complete the function tiltTree(), that return the tilt of the whole tree. The tilt of a tree node
is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values. Null nodes are assigned
tilt to be zero. Therefore, tilt of the whole tree is defined as the sum of all nodes’ tilt.

Examples 1:

Input: 
       1
      / \
     2   3
Output: 1
Explanation:
Tilt of node 2 : 0
Tilt of node 3 : 0
Tilt of node 1 : |2-3| = 1
Tilt of binary tree : 0 + 0 + 1 = 1
'''

class Solution:
    def tiltTree(self,root):
        def traversal(root):
            nonlocal total
            
            if root==None:
                return 0
                
            ls=traversal(root.left)
            rs=traversal(root.right)
            
            sum1=ls+rs+root.data
        
            total+=abs(ls-rs)
            
            return sum1
            
        total=0
        
        traversal(root)
        
        return total
