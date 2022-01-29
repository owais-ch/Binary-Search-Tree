'''Given a Binary Search Tree. Find sum of all elements smaller than and equal to Kth smallest element.

Example 1:

Input: 
          20
        /    \
       8     22
     /    \
    4     12
         /    \
        10    14   , K=3

Output: 22
Explanation:
Sum of 3 smallest elements are: 
4 + 8 + 10 = 22'''

import numpy as np

def sum(root, k):
    list1=[]
    def traversal(root):
        if root.left:
            traversal(root.left)
            
        list1.append(root.key)
        
        if root.right:
            traversal(root.right)
            
    traversal(root)
    
    return np.sum(list1[:k])
