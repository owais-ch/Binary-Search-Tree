'''Given a BST and an integer. Find the least absolute difference between any node value of the BST and the given integer.

Example 1:

Input:
        10
      /   \
     2    11
   /  \ 
  1    5
      /  \
     3    6
      \
       4
K = 13
Output: 2
Explanation: K=13. The node that has
value nearest to K is 11. so the answer
is 2'''


class Solution:
    def __init__(self):
        self.list1=[]
    def minDiff(self,root, K):
        def traversal(root):
            if root.left:
                traversal(root.left)
            
            self.list1.append(root.data)
            
            if root.right:
                traversal(root.right)
                
        traversal(root)
        
        length=len(self.list1)
        
        minimum=999999
        
        for i in range(length):
            minimum=min(minimum,abs(self.list1[i]-K))
            
        return minimum
