'''Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:

Input: root = [3,1,4,null,2], k = 1
Output: 1'''

class Solution:
    def __init__(self):
        self.list1=[]
    def kthSmallest(self, root, k):
        self.list1.append(root.val)
        
        if root.left:
            self.kthSmallest(root.left,k)
            
        if root.right:
            self.kthSmallest(root.right,k)
        self.list1.sort() 
        if k>len(self.list1):
            return None
        return self.list1[k-1]
