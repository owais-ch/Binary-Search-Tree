'''Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

Example 1:

Input: root = [4,2,6,1,3]
Output: 1'''

class Solution:
    def __init__(self):
        self.list1=[]
    def minDiffInBST(self, root):
        self.list1.append(root.val)
        
        if root.left:
            self.minDiffInBST(root.left)
            
        if root.right:
            self.minDiffInBST(root.right)
            
        length=len(self.list1)
        
        minimum=9999999
        for i in range(length-1):
            for j in range(i+1,length):
                minimum=min(abs(self.list1[i]-self.list1[j]),minimum)
                
        return minimum
