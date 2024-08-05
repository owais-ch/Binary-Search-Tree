'''
Max Level Sum in Binary Tree (GFG)

Given a Binary Tree having positive and negative nodes. Find the maximum sum of a level in the given Binary Tree.

Example 1:

Input :               
             4
          /    \
         2     -5
        / \    / \
      -1   3  -2  6

Output: 6
'''

import math

class Solution:
    def maxLevelSum(self, root):
        def height(root,h):
            if root==None:
                return None
                
            if h not in dict1:
                dict1[h]=root.data
            else:
                dict1[h]+=root.data
                
            if root.left:
                height(root.left,h+1)
                
            if root.right:
                height(root.right,h+1)
                
        dict1=dict()
        
        height(root,0)
        
        maximum=-math.inf
        
        for i in dict1:
            if dict1[i]>maximum:
                maximum=dict1[i]
                
        return maximum
