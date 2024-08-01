''
Minimum Absolute Difference In BST (GFG)

Given a binary search tree having n (n>1) nodes, the task is to find the minimum absolute difference between any two nodes.
'''

import math

class Solution:
    def absolute_diff(self,root):
        def traversal(root):
            nonlocal minimum,count,first,second
            if root==None:
                return None
                
            if root.left:
                traversal(root.left)
                
            if count==0:
                first=root.data
                count+=1
            else:
                second=root.data
                diff=second-first
                if diff<minimum:
                    minimum=diff
                first=root.data
            
            if root.right:
                traversal(root.right)
                
        minimum=math.inf
        count=0
        first,second=0,0
        traversal(root)
        
        return minimum
