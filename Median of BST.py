'''Given a Binary Search Tree of size N, find the Median of its Node values.

Example 1:

Input:
       6
     /   \
   3      8   
 /  \    /  \
1    4  7    9
Output: 6
Explanation: Inorder of Given BST will be:
1, 3, 4, 6, 7, 8, 9. So, here median will 6.'''

import numpy as np

def findMedian(root):
    list1=[]
    
    def traversal(root):
        if root.left:
            traversal(root.left)
            
        list1.append(root.data)
        
        if root.right:
            traversal(root.right)
            
    traversal(root)
    
    if int(np.median(list1))==np.median(list1):
        return int(np.median(list1))
    else:
        return np.median(list1)
