'''Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.

Example 1:
  
Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].'''

import numpy as np

class Solution:
    def averageOfLevels(self, root) -> List[float]:
        def height(root):
            if root==None:
                return 0
            left=height(root.left)
            right=height(root.right)
            
            return max(left,right)+1
        
        def traversal(root,level):
            nonlocal count
            if root==None:
                return None
            
            if level==0:
                list1[count].append(root.val)
            else:
                traversal(root.left,level-1)
                traversal(root.right,level-1)
                
        tall=height(root)
        list1=[[] for i in range(tall)]
        list2=[]
        count=0
        
        for i in range(tall):
            traversal(root,i)
            list2.append(np.mean(list1[count]))
            count+=1
            
        return list2
