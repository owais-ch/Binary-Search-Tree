'''Given a Binary search tree. Your task is to complete the function which will return the Kth largest element without doing any modification in Binary Search Tree.

Example 1:

Input:
      4
    /   \
   2     9
k = 2 
Output: 4'''

class Solution:
    def __init__(self):
        self.list1=[]
    def kthLargest(self,root, k):
        def traversal(root):
            if root.left:
                traversal(root.left)
                
            self.list1.append(root.data)
            
            if root.right:
                traversal(root.right)
                
        traversal(root)
        
        if k>len(self.list1):
            return -1
            
        return self.list1[-k]
