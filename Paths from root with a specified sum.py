'''Given a Binary tree and a sum S, print all the paths, starting from root, that sums upto the given sum. Path maynot end on a leaf node.

Example 1:

Input : 
sum = 8,
Root of tree
         1
       /   \
     20      3
           /    \
         4       15   
        /  \     /  \
       6    7   8    9      

Output :
1 3 4
Explanation : 
Sum of path 1, 3, 4 = 8.'''


import numpy as np
class Solution:
    def printPaths(self, root, sum1):
        
        def traversal(root):
            nonlocal sum2
            
            if root==None:
                return None
            
            stack.append(root.data) 
            sum2=sum2+root.data
            if root.left:
                traversal(root.left)
            
            if sum2==sum1:
                list1.append(stack.copy())
                
            if root.right:
                traversal(root.right)
            
            sum2=sum2-stack[-1]    
            stack.pop()
            
        stack=[]
        list1=[]
        sum2=0
        traversal(root)
        
        return list1
