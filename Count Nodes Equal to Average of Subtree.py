'''Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.

Note:

The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
A subtree of root is a tree consisting of root and all of its descendants.
 

Example 1:


Input: root = [4,8,5,0,1,null,6]
Output: 5
Explanation: 
For the node with value 4: The average of its subtree is (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4.
For the node with value 5: The average of its subtree is (5 + 6) / 2 = 11 / 2 = 5.
For the node with value 0: The average of its subtree is 0 / 1 = 0.
For the node with value 1: The average of its subtree is 1 / 1 = 1.
For the node with value 6: The average of its subtree is 6 / 1 = 6.'''

from math import floor

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def traversal(root,count):
            nonlocal countz
            if root==None:
                #count+=1
                return [0,count]
            
            ls=traversal(root.left,count)
            rs=traversal(root.right,count)

            sum1=root.val+ls[0]+rs[0]
            total=ls[1]+rs[1]+1
            count=total
            
            average=floor(sum1/total)

            if average==root.val:
                countz+=1
            return sum1,count
            
        countz=0
        traversal(root,0)

        return countz
