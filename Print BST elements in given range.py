'''Given a Binary Search Tree and a range [low, high]. Find all the numbers in the BST that lie in the given range.
Note: Element greater than or equal to root go to the right side.

Example 1:

Input:
       17
     /    \
    4     18
  /   \
 2     9 
l = 4, h = 24
Output: 4 9 17 18 '''

class Solution:
    def __init__(self):
        self.list1=[]
    def printNearNodes(self, root, low, high):
        def traversal(root):
            if root.left:
                traversal(root.left)
                
            self.list1.append(root.data)
            
            if root.right:
                traversal(root.right)
                
        traversal(root)
        
        length=len(self.list1)
        
        list2=[]
        
        for i in range(length):
            if self.list1[i]>=low and self.list1[i]<=high:
                list2.append(self.list1[i])
                
        return list2
