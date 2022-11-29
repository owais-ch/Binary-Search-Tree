'''In an online game, N blocks are arranged in a hierarchical manner. All the blocks are connected together by a total of N-1 connections. Each block is given
an ID from 1 to N. A block may be further connected to other blocks. Each block is also assigned a specific point value.

A player starts from Block 1. She must move forward from each block to a directly connected block until she reaches the final block, which has no further
connection. When the player lands on a block, she collects the point value of that block. The players score is calculated as the product of point values that the 
player collects.
Find the maximum score a player can achieve.
Note: The answer can always be represented with 64 bits.


Example 1:

Input:
     4
    / \
   2   8
  / \ / \
 2  1 3  4
Output: 128
Explanation: Path in the given tree 
goes like 4, 8, 4 which gives the max
score of 4x8x4 = 128.
'''

class Solution:
    def findMaxScore(self, root):
        def traversal(root):
            nonlocal product,maximum
            
            if root==None:
                return None
                
            product=product*root.data
            
            if root.left==None and root.right==None:
                maximum=max(maximum,product)
                
            if traversal(root.left) or traversal(root.right):
                return True
                
            product=product/root.data
            
            return False
            
        product=1
        maximum=-999999
        traversal(root)
        
        return int(maximum)
